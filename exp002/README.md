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
| 01 |  |  |  | box, m_range=2, image_size=32, image_channel=1, num_frame=3, bg_move |
| 01-1 |  |  |  | box_complex, m_range=2, image_size=32, image_channel=1, num_frame=3, bg_move |
| 02 |  |  |  | mnist, m_range=2, image_size=32, image_channel=1, num_frame=3, bg_move |
| 03 |  |  |  | robot64, m_range=2, image_size=64, image_channel=1, num_frame=3 |
| 04 |  |  |  | mpii64, m_range=2, image_size=64, image_channel=1, num_frame=3 |
| 05 |  |  |  | nyuv2, m_range=2, image_size=64, image_channel=1, num_frame=3 |

### Take Home Message

