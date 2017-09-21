## Normalize Weight - 3 Frame 

- Occlusion modeling, contribution of all pixels at every location will be normalized to 1, unless not enough to 1 
- Predict motion for every pixel
- Photometric loss for pixels that are not occluded, then divided by the total number of existing pixels
- Input 2 frames
- Output is 3rd frame
- Color image

### Results

- Column 2 and 3: Improve reconstruction loss over baseline (%) 

| Exp  | Test | Gt   | EPE  | Note |
| ---- | ---- | ---- | ---- | ---- | 
| 01   | 0.98 | 0.94 | 0.12 | box, m_range=2, image_size=32, num_frame=3, bg_move |
| 01-1 | 0.95 | 0.95 | 0.16 | box, m_range=2, image_size=32, num_frame=3, bg_move |
| 02   | 0.96 | 0.93 | 0.14 | mnist, m_range=2, image_size=32, num_frame=3, bg_move |
| 03   | 0.23 |  |  | robot64, m_range=2, image_size=64, num_frame=3 |
| 04   | 0.26 |  |  | mpii64, m_range=2, image_size=64, num_frame=3 |
| 05   | 0.22 |  |  | nyuv2, m_range=2, image_size=64, num_frame=3 |

### Take Home Message

