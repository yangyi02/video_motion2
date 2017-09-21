## Loose Loss - 3 Frame 

- No occlusion modeling
- Predict motion for every pixel
- Photometric loss for pixels that are not occluded and not conflicted, then divided by the total number of ok pixels
- Input 2 frames
- Output is 3rd frame
- Color image

### Results

- Column 2 and 3: Improve reconstruction loss over baseline (%) 

| Exp  | Test | Gt   | EPE  | Note |
| ---- | ---- | ---- | ---- | ---- | 
| 01   | 0.99 | 1.00 | 0.06 | box, m_range=2, image_size=32, num_frame=3, bg_move |
| 01-1 | 0.95 | 1.00 | 0.16 | box_complex, m_range=2, image_size=32, num_frame=3, bg_move |
| 02   | 0.98 | 1.00 | 0.06 | mnist, m_range=2, image_size=32, num_frame=3, bg_move |
| 03   | 0.31 |  |  | robot64, m_range=2, image_size=64, num_frame=3 |
| 04   | 0.34 |  |  | mpii64, m_range=2, image_size=64, num_frame=3 |
| 05   | 0.26 |  |  | nyuv2, m_range=2, image_size=64, num_frame=3 |

### Take Home Message

