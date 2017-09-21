## Simplest Experiment - 3 Frame

- Predict motion for every pixel
- Photometric loss for every pixel
- Input 2 frames
- Output is 3rd frame
- Color image

### Results

- Column 2 and 3: Improve reconstruction loss over baseline (%) 

| Exp  | Test | Gt   | EPE  | Note |
| ---- | ---- | ---- | ---- | ---- | 
| 01   | 0.82 | 0.78 | 0.18 | box, m_range=2, image_size=32, num_frame=3, bg_move |
| 01-1 | 0.66 | 0.49 | 0.74 | box_complex, m_range=2, image_size=32, num_frame=3, bg_move |
| 02   | 0.82 | 0.78 | 0.23 | mnist, m_range=2, image_size=32, num_frame=3, bg_move |
| 03   | 0.28 |  |  | robot64, m_range=2, image_size=64, num_frame=3 |
| 04   | 0.28 |  |  | mpii64, m_range=2, image_size=64, num_frame=3 |
| 05   | 0.29 |  |  | nyuv2, m_range=2, image_size=64, num_frame=3 |

### Take Home Message

