## Baseline Experiment - 2 Frame 

- Occlusion modeling, moving pixels will occlude static pixels
- Predict motion for every pixel
- Photometric loss for pixels that are not occluded, then divided by the total number of existing pixels
- Input 2 frames
- Output is 2nd frame, the ouput is also an input of itself
- Color image

### Results

- Column 2 and 3: Improve reconstruction loss over baseline (%) 

| Exp  | Test | Gt   | EPE  | Note |
| ---- | ---- | ---- | ---- | ---- | 
| 01   | 0.99 | 0.94 | 0.13 | box, m_range=2, image_size=32, num_frame=2, bg_move |
| 01-1 | 0.95 | 0.86 | 0.19 | box_complex, m_range=2, image_size=32, num_frame=2, bg_move |
| 02   | 0.94 | 0.92 | 0.32 | mnist, m_range=2, image_size=32, num_frame=2, bg_move |
| 03   | 0.53 |  |  | robot64, m_range=2, image_size=64, num_frame=2 |
| 04   | 0.63 |  |  | mpii64, m_range=2, image_size=64, num_frame=2 |
| 05   | 0.57 |  |  | nyuv2, m_range=2, image_size=64, num_frame=2 |

### Take Home Message

