## Predict Occlusion - 2 Frame 

- Occlusion modeling, use neural net to predict occlusion pixels 
- Predict motion for every pixel
- Photometric loss for pixels that are not occluded, then divided by the total number of existing pixels
- Input 2 frames
- Output is 2nd frame, the ouput is also an input of itself
- Color image

### Results

- Column 2 and 3: Improve reconstruction loss over baseline (%) 

| Exp  | Test | Gt   | EPE  | Note |
| ---- | ---- | ---- | ---- | ---- | 
| 01   | 0.98 |  | 0.16 | box, m_range=2, image_size=32, num_frame=2, bg_move |
| 01-1 | 0.96 |  | 0.38 | box_complex, m_range=2, image_size=32, num_frame=2, bg_move |
| 02   | 0.98 |  | 0.12 | mnist, m_range=2, image_size=32, num_frame=2, bg_move |
| 03   |      |  |  | robot64, m_range=2, image_size=64, num_frame=2 |
| 04   | 0.51 |  |  | mpii64, m_range=2, image_size=64, num_frame=2 |
| 05   |      |  |  | nyuv2, m_range=2, image_size=64, num_frame=2 |

### Take Home Message

