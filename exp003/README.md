## Simplest Experiment - 2 Frame

- Predict motion for every pixel
- Photometric loss for every pixel
- Input 2 frames
- Output is 2nd frame, the ouput is also an input of itself
- Color image

### Results

- Column 2 and 3: Improve reconstruction loss over baseline (%) 

| Exp  | Test | Gt   | EPE  | Note |
| ---- | ---- | ---- | ---- | ---- | 
| 01   | 0.83 | 0.77 | 0.26 | box, m_range=2, image_size=32, num_frame=2, bg_move |
| 01-1 | 0.68 | 0.48 | 0.81 | box_complex, m_range=2, image_size=32, num_frame=2, bg_move |
| 02   | 0.84 | 0.77 | 0.33 | mnist, m_range=2, image_size=32, num_frame=2, bg_move |
| 03   | 0.60 |  |  | robot64, m_range=2, image_size=64, num_frame=2 |
| 04   | 0.66 |  |  | mpii64, m_range=2, image_size=64, num_frame=2 |
| 05   | 0.58 |  |  | nyuv2, m_range=2, image_size=64, num_frame=2 |

### Take Home Message

