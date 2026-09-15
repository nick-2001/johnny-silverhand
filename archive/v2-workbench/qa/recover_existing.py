from PIL import Image
from pathlib import Path
import json, shutil
R=Path(__file__).resolve().parents[1]
im=Image.open(R.parents[1] / 'assets/source/relic-bust.png').convert('RGBA')
states=['idle','running-right','running-left','waving','jumping','failed','waiting','running','review']
bounds=[0,145,285,427,576,722,868,1018,1185,1385]
selected=[[0,1,2,3,4,5],list(range(8)),list(range(8)),[0,2,4,6],[0,1,2,3,6],list(range(8)),[0,1,2,3,4,5],[0,1,2,3,4,5],[0,1,2,3,4,5]]
rows=[]
for r,state in enumerate(states):
 d=R/'frames'/state;d.mkdir(parents=True,exist_ok=True)
 for p in d.glob('*.png'):p.unlink()
 for j,c in enumerate(selected[r]):
  # Exact original pixels; no resampling, repainting, warping or pose synthesis.
  tile=im.crop((c*142,bounds[r],(c+1)*142,bounds[r+1]))
  # Exclude source's isolated final scanline artifact, outside its hologram body.
  if r==8:tile=tile.crop((0,0,142,194))
  out=Image.new('RGBA',(192,208));out.alpha_composite(tile,(25,200-tile.height));out.save(d/f'{j:02d}.png')
 rows.append({'state':state,'method':'stable-slots','source_row':r,'source_y_bounds':bounds[r:r+2],'source_columns':selected[r],'scale':1.0,'baseline':200})
(R/'frames/frames-manifest.json').write_text(json.dumps({'source':str(im.filename) if hasattr(im,'filename') else 'source-relic-bust.png','rows':rows},indent=2))
for sub in ['references','decoded','final']: (R/sub).mkdir(exist_ok=True)
shutil.copyfile(R/'frames/idle/00.png',R/'references/canonical-base.png')
shutil.copyfile(R/'frames/idle/00.png',R/'decoded/base.png')
