## Simplest Experiment - 2 Frame, Gray Scale

- Predict motion for every pixel
- Photometric loss for every pixel
- Input 2 frames
- Output is 2nd frame, the ouput is also an input of itself
- Gray scale image

### Results

- Column 2 and 3: Improve reconstruction loss over baseline (%) 

| Exp  | Test | Gt   | EPE  | Note |
| ---- | ---- | ---- | ---- | ---- | 
| 01   | 0.96 | 0.77 | 1.73 | box, m_range=2, image_size=32, image_channel=1, num_frame=2, bg_move |
| 01-1 | 0.93 | 0.47 | 1.92 | box_complex, m_range=2, image_size=32, image_channel=1, num_frame=2, bg_move |
| 02   | 0.97 | 0.77 | 1.81 | mnist, m_range=2, image_size=32, image_channel=1, num_frame=2, bg_move |
| 03   | 0.87 |  |  | robot64, m_range=2, image_size=64, image_channel=1, num_frame=2 |
| 04   | 0.83 |  |  | mpii64, m_range=2, image_size=64, image_channel=1, num_frame=2 |
| 05   | 0.77 |  |  | nyuv2, m_range=2, image_size=64, image_channel=1, num_frame=2 |

### Take Home Message

