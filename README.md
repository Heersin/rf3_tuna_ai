# rf3_tuna_ai
Rune Factory 3 -- Tuna, Generate By so-vits-svc 4.0

## Instructions
1. raw_data from [tieba](https://www.tieba.com/p/8292995224)

2. filter by wav.title attributes which contains 'myce'

3. trained by [so-vits-svc](https://github.com/svc-develop-team/so-vits-svc)
    - about 58000 steps, V100 GPU * 1 for 10+ hours (cloud server)
        - cuda 12 and torch 1.13.1
    - pretrained model and env from hugging_face
        - D_0.pth and G_0.pth
        - 44k
    - kmeans cluster used

4. music vocal extraction, try the following:
    - online : [melody ML](https://melody.ml/) and [vocal remover](https://vocalremover.org/)
    - local: deploy [uvr5-gui](https://github.com/Heersin/ultimatevocalremovergui) on linux, 3080Ti 3-4 minutes per song
        - window size : 320
        - VR-HP-3 model 

5. inference command:
    `python inference_main.py -m "logs/44k/G_[step].pth" -c "configs/config.json" -n "[song].wav" -t 0 -s "[speaker]" -cm "logs/44k/kmeans_10000.pth" -cr 0.4`

6. Mix vocal and intrumental/bass/drums ...: Audacity

7. Picture Generate NovelAI

8. Video maker : kdenlive

## Result
```
无知时诋毁图恒宇
懂事时理解图恒宇
成熟时成为图恒宇
```

<audio id="audio" controls="" preload="none"><source id="m4a" src="https://github.com/Heersin/rf3_tuna_ai/raw/main/life_mix.wav"></audio>

## Celebration
[Rune Factory3 for NS](https://asia.sega.com/rf3sp/cn/) ! Looking forward to new game also.
