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
| 01 |  |  |  | box, m_range=2, image_size=32, image_channel=1, num_frame=2, bg_move |
| 01-1 |  |  |  | box_complex, m_range=2, image_size=32, image_channel=1, num_frame=2, bg_move |
| 02 |  |  |  | mnist, m_range=2, image_size=32, image_channel=1, num_frame=2, bg_move |
| 03 |  |  |  | robot64, m_range=2, image_size=64, image_channel=1, num_frame=2 |
| 04 |  |  |  | mpii64, m_range=2, image_size=64, image_channel=1, num_frame=2 |
| 05 |  |  |  | nyuv2, m_range=2, image_size=64, image_channel=1, num_frame=2 |

### Take Home Message

