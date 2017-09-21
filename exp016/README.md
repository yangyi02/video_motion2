## Predict Depth - 3 Frame 

- Occlusion modeling, use neural net to predict discrete depth 
- Predict depth using only current frame with another network
- Predict motion for every pixel
- Photometric loss for pixels that are not occluded, then divided by the total number of existing pixels
- Input 2 frames
- Output is 3rd frame
- Color image

### Results

- Column 2 and 3: Improve reconstruction loss over baseline (%) 

| Exp  | Test | Gt   | EPE  | Note |
| ---- | ---- | ---- | ---- | ---- | 
| 01   | 1.00 | 1.00 | 0.02 | box, m_range=2, image_size=32, num_frame=3, bg_move |
| 01-1 | 0.98 | 1.00 | 0.07 | box_complex, m_range=2, image_size=32, num_frame=3, bg_move |
| 02   | 0.98 | 1.00 | 0.05 | mnist, m_range=2, image_size=32, num_frame=3, bg_move |
| 03   | 0.24 |  |  | robot64, m_range=2, image_size=64, num_frame=3 |
| 04   | 0.30 |  |  | mpii64, m_range=2, image_size=64, num_frame=3 |
| 05   | 0.23 |  |  | nyuv2, m_range=2, image_size=64, num_frame=3 |

### Take Home Message

