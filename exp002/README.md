## Simplest Experiment - 3 Frame, Gray Scale

- Predict motion for every pixel
- Photometric loss for every pixel
- Input 2 frames
- Output is 3rd frame
- Gray scale image

### Results

- Column 2 and 3: Improve reconstruction loss over baseline (%) 

| Exp  | Test | Gt   | EPE  | Note |
| ---- | ---- | ---- | ---- | ---- | 
| 01   | 0.83 | 0.78 | 0.20 | box, m_range=2, image_size=32, image_channel=1, num_frame=3, bg_move |
| 01-1 | 0.76 | 0.48 | 1.30 | box_complex, m_range=2, image_size=32, image_channel=1, num_frame=3, bg_move |
| 02   | 0.82 | 0.78 | 0.30 | mnist, m_range=2, image_size=32, image_channel=1, num_frame=3, bg_move |
| 03   | 0.39 |  |  | robot64, m_range=2, image_size=64, image_channel=1, num_frame=3 |
| 04   | 0.32 |  |  | mpii64, m_range=2, image_size=64, image_channel=1, num_frame=3 |
| 05   | 0.23 |  |  | nyuv2, m_range=2, image_size=64, image_channel=1, num_frame=3 |

### Take Home Message

