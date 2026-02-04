# Chat: Finding DNS Bhat Videos on @MALATIBHAT YouTube Channel

## User

Can you find all posted videos/playlists on https://www.youtube.com/@MALATIBHAT that reference DNS Bhat (Shankhar bhat)'s books?

## Assistant

Attempted to fetch the YouTube channel directly via WebFetch, but YouTube is blocked for direct fetching. Ran multiple web searches with various query combinations:

- `site:youtube.com "@MALATIBHAT" "DNS Bhat" OR "Shankar Bhat" OR "D.N.S. Bhat" books`
- `youtube.com MALATIBHAT channel DNS Bhat Shankar Bhat books playlist`
- `"MALATI BHAT" youtube kannada DNS Shankar Bhat`
- `youtube "Malati Bhat" "ಶಂಕರ ಬಟ್" OR "shankar bhat" playlist`

Search results revealed:
- Malati Bhat authored "SPOKEN ENGLISH KANNADA" (Parts 1 & 2) and "Why Kannada Needs Its Own Grammar"
- Dr. D.N. Shankara Bhat is a world-renowned Kannada linguist with 25+ books
- His official website is dnshankarabhat.net
- The DNS Bhat website has a videos section (ವಿಡಿಯೋಗಳು)

Also fetched https://dnshankarabhat.net/books/ which listed 20+ Kannada titles and several English titles by DNS Bhat. No mention of Malati Bhat or YouTube on that site.

Web search results could not directly index the @MALATIBHAT YouTube channel content.

## User

(Clarified that the channel exists at https://www.youtube.com/@MALATIBHAT/videos and only a subset of videos are about DNS Bhat's books.)

## Assistant

Installed `yt-dlp` via Homebrew and extracted the full video list from the channel:

```
yt-dlp --flat-playlist --print "%(title)s ||| %(id)s ||| %(description)s" "https://www.youtube.com/@MALATIBHAT/videos"
```

This returned a large output (721.8KB) with all video titles, IDs, and descriptions. Filtered for DNS Bhat references using grep and found hundreds of matching videos.

Key discovery from the video descriptions:
> "I am Malati Bhat, daughter of Prof.DNS Bhat. I will be reading one of his books..."

### Results: Book Reading Series

| # | Book Title | Episodes |
|---|-----------|----------|
| 1 | **IDU KANNADADE VYAKARANA** (ಇದು ಕನ್ನಡದೆ ವ್ಯಾಕರಣ) | 3 parts |
| 2 | **KANNADALLE HOSAPADAGALANNU KATTUVA BAGE** (ಕನ್ನಡದಲ್ಲಿ ಹೊಸಪದಗಳನ್ನು ಕಟ್ಟುವ ಬಗೆ) | 52 parts |
| 3 | **KANNADA PADAGALA OLARACHANE** (ಕನ್ನಡ ಪದಗಳ ಒಳರಚನೆ) | 55 parts |
| 4 | **MATHU MATTHU BARAHADA NADUVINA GONDALA** (ಮಾತು ಮತ್ತು ಬರಹದ ನಡುವಿನ ಗೊಂದಲ) | 44 parts |
| 5 | **MATHINA OLAGUTTU** (ಮಾತಿನ ಒಳಗುಟ್ಟು) | 37 parts |
| 6 | **KALIKENUDI MATTHU NUDIKALIKE** (ಕಲಿಕೆನುಡಿ ಮತ್ತು ನುಡಿಕಲಿಕೆ) | 21 parts |
| 7 | **KANNADADA SOLLARIME** (ಕನ್ನಡದ ಸೊಲ್ಲರಿಮೆ) | 23 parts |
| 8 | **KANNADAKKE MAHAPRANA YAKE BEDA** (ಕನ್ನಡಕ್ಕೆ ಮಹಾಪ್ರಾಣ ಯಾಕೆ ಬೇಡ) | 19 parts |
| 9 | **HAVYAKA KANNADA** (ಹವ್ಯಕ ಕನ್ನಡ) | 43 parts |
| 10 | **KANNADA NUDIYA HINNADAVALI** (ಕನ್ನಡ ನುಡಿಯ ಹಿನ್ನಡವಳಿ) | 14 parts |
| 11 | **KANNADA BARAHADA PADASAMASYE** (ಕನ್ನಡ ಬರಹದ ಪದಸಮಸ್ಯೆ) | 25 parts |
| 12 | **KANNADA BHASHEYA KALPITA CHARITRE** (ಕನ್ನಡ ಭಾಷೆಯ ಕಲ್ಪಿತ ಚರಿತ್ರೆ) | 2 parts |
| 13 | **DHAREGE DODDAVARU** (read by Meti Mallikarjun) | 4 parts |

### Standalone Videos about DNS Bhat

- **DNS BHAT : First Interview** (4 parts)
- **DNS BHAT BOOKS**
- **Prof. DNS BHAT "Read my books...Everything is explained there."**
- **Shambha Joshi award to Dr.D.N.S.Bhat**
- **DNS BHAT interview by AKSHARA of NINASAM**
- **DNS BHAT explains why 31 letters are enough in KANNADA alphabet**
- **HOSA BARAHA (new writing) FOR KANNADA**
- **BOOK RELEASE FUNCTION : DNS BHAT : KANNADA BARAHADA PADASAMASYE**

### Shorts Series (61+ shorts)

Topics from DNS Bhat's writings covering: teaching English to children, Ellara Kannada, Sanskrit vs Kannada, computer translation, script reform, etc. (labeled 1S through 61S).

### Bharathi Bhat (wife of DNS Bhat) - Related Videos

- **ಮನೆಗೆಲಸದ ಕೈಪಿಡಿ** (Household Handbook)
- **ಅಮೆರಿಕನರ ವ್ಯಾಪಾರ ಚಾಕಚಕ್ಯತೆ** (American Business Acumen)
- **ಟಿ. ವಿ. ರೆಪೇರಿ** (TV Repair)
- **ಬದುಕು ಬರಹ** (Life and Writing)

In total, there are **hundreds** of videos on this channel referencing DNS Bhat's books -- the channel is essentially a spoken-word library of Prof. D.N.S. Bhat's entire body of Kannada linguistic works.

---

## User

In the table add another column, which lists the hyperlinks to the individual videos.

## Assistant

Extracted video IDs for each series using grep on the yt-dlp output, then constructed YouTube URLs for every video.

### Book Reading Series (with links)

#### 1. IDU KANNADADE VYAKARANA (ಇದು ಕನ್ನಡದೆ ವ್ಯಾಕರಣ) - 3 parts

| # | Link |
|---|------|
| 1 | https://www.youtube.com/watch?v=wBaRf2lMGic |
| 2 | https://www.youtube.com/watch?v=h5VFWQQfPO8 |
| 3 | https://www.youtube.com/watch?v=6EBf9mJG4qI |

#### 2. KANNADALLE HOSAPADAGALANNU KATTUVA BAGE (ಕನ್ನಡದಲ್ಲಿ ಹೊಸಪದಗಳನ್ನು ಕಟ್ಟುವ ಬಗೆ) - 52 parts

| # | Link |
|---|------|
| 1 | https://www.youtube.com/watch?v=zQ_fDKwmd18 |
| 2 | https://www.youtube.com/watch?v=-LZCAEGkI8Y |
| 3 | https://www.youtube.com/watch?v=LxCYKEXQ8pY |
| 4 | https://www.youtube.com/watch?v=f_GPodk6JPU |
| 5 | https://www.youtube.com/watch?v=DhBOx9Wjp5s |
| 6 | https://www.youtube.com/watch?v=0L7q5hy9w4c |
| 7 | https://www.youtube.com/watch?v=-oaKzIRSd5U |
| 8 | https://www.youtube.com/watch?v=N46zhYoQN-M |
| 9 | https://www.youtube.com/watch?v=haxjaBc_N3Y |
| 10 | https://www.youtube.com/watch?v=nj-CXSrO84A |
| 11 | https://www.youtube.com/watch?v=iTk7pWqFzVs |
| 12 | https://www.youtube.com/watch?v=3MkOfKh3pNY |
| 13 | https://www.youtube.com/watch?v=R5mwgOJ-CQA |
| 14 | https://www.youtube.com/watch?v=bgvYILSqs-0 |
| 15 | https://www.youtube.com/watch?v=UuCLvjJnVmo |
| 16 | https://www.youtube.com/watch?v=hsoIu6hoz4I |
| 17 | https://www.youtube.com/watch?v=kNj0cN_yDfQ |
| 18 | https://www.youtube.com/watch?v=udmNBzzw5bg |
| 20 | https://www.youtube.com/watch?v=l8jnzk6sRSg |
| 21 | https://www.youtube.com/watch?v=FLcf3GHiUv4 |
| 22 | https://www.youtube.com/watch?v=M8MDflNE5-s |
| 23 | https://www.youtube.com/watch?v=Y7xKg-LyKJU |
| 24 | https://www.youtube.com/watch?v=TE7xB8es8eo |
| 25 | https://www.youtube.com/watch?v=-D7SBeaTplU |
| 26 | https://www.youtube.com/watch?v=qF4LxHKbkK4 |
| 27 | https://www.youtube.com/watch?v=JAJX40OHnFg |
| 28 | https://www.youtube.com/watch?v=KaNjJy8rqrI |
| 29 | https://www.youtube.com/watch?v=OdLHO0oM400 |
| 30 | https://www.youtube.com/watch?v=gVT-3NbnEQo |
| 31 | https://www.youtube.com/watch?v=jvz6LnLaYQ0 |
| 32 | https://www.youtube.com/watch?v=_m3WEXor1nI |
| 33 | https://www.youtube.com/watch?v=QmvEkwyLvco |
| 34 | https://www.youtube.com/watch?v=ctrM_s5vl2s |
| 35 | https://www.youtube.com/watch?v=do5fe09_srk |
| 36 | https://www.youtube.com/watch?v=Obchh_UVAN0 |
| 37 | https://www.youtube.com/watch?v=ce6Ld3GXN7Q |
| 38 | https://www.youtube.com/watch?v=RPwnp023Ags |
| 39 | https://www.youtube.com/watch?v=ABEFlZz-LBo |
| 40 | https://www.youtube.com/watch?v=cyytEAJgaw0 |
| 41 | https://www.youtube.com/watch?v=QblcTVypDdo |
| 42 | https://www.youtube.com/watch?v=bkE4-c0hYuk |
| 43 | https://www.youtube.com/watch?v=yqJF7NfNlnE |
| 44 | https://www.youtube.com/watch?v=LLFi4ToEl-o |
| 45 | https://www.youtube.com/watch?v=bn-fVa90GQ8 |
| 46 | https://www.youtube.com/watch?v=n03Q2lS7fkk |
| 47 | https://www.youtube.com/watch?v=0Wo-pNtEfn0 |
| 48 | https://www.youtube.com/watch?v=Rs7RS9PRZ8M |
| 49 | https://www.youtube.com/watch?v=NhU9XTHztFg |
| 50 | https://www.youtube.com/watch?v=Xd5kuZtekd8 |
| 51 | https://www.youtube.com/watch?v=6ZMx9OWw11Y |
| 52 | https://www.youtube.com/watch?v=ymWjyCxhsFo |

#### 3. KANNADA PADAGALA OLARACHANE (ಕನ್ನಡ ಪದಗಳ ಒಳರಚನೆ) - 55 parts

| # | Link |
|---|------|
| 1 | https://www.youtube.com/watch?v=9E_vy5ZMlwY |
| 2 | https://www.youtube.com/watch?v=hm6-5EhEc-8 |
| 3 | https://www.youtube.com/watch?v=z2li4n30Qv8 |
| 4 | https://www.youtube.com/watch?v=kO1t84LR0tY |
| 5 | https://www.youtube.com/watch?v=kkQenbxSqdU |
| 6 | https://www.youtube.com/watch?v=2s2cQxh7lyc |
| 7 | https://www.youtube.com/watch?v=D6tyINsbw0s |
| 8 | https://www.youtube.com/watch?v=9caMwEb23GQ |
| 9 | https://www.youtube.com/watch?v=B9LNvrMssjM |
| 10 | https://www.youtube.com/watch?v=ZF_ECohh3gs |
| 11 | https://www.youtube.com/watch?v=0DgxLN27pQk |
| 12 | https://www.youtube.com/watch?v=OwadkPLBGic |
| 13 | https://www.youtube.com/watch?v=m5ZOPctIHxI |
| 14 | https://www.youtube.com/watch?v=6Vx9nrn0QB0 |
| 15 | https://www.youtube.com/watch?v=UU4GBIBe2V4 |
| 16 | https://www.youtube.com/watch?v=AXTXAO9K_6Q |
| 17 | https://www.youtube.com/watch?v=z77gcGRFX9I |
| 18 | https://www.youtube.com/watch?v=bZLEALkygyU |
| 19 | https://www.youtube.com/watch?v=c8lyxJd6n6A |
| 20 | https://www.youtube.com/watch?v=8zHSrsZHrhk |
| 21 | https://www.youtube.com/watch?v=sav8TgXWpXA |
| 22 | https://www.youtube.com/watch?v=TjX74ddij3w |
| 23 | https://www.youtube.com/watch?v=hZ3AHdQRTUY |
| 24 | https://www.youtube.com/watch?v=6dqModFb7e0 |
| 25 | https://www.youtube.com/watch?v=w61-wN3neY4 |
| 26 | https://www.youtube.com/watch?v=mu7C4Ys9UtI |
| 27 | https://www.youtube.com/watch?v=JVcjLYC7mW8 |
| 28 | https://www.youtube.com/watch?v=hnAtyOvx_LI |
| 29 | https://www.youtube.com/watch?v=sMrRgGMYof4 |
| 30 | https://www.youtube.com/watch?v=9RvlR_j5dL8 |
| 31 | https://www.youtube.com/watch?v=zJHwH-xkfFs |
| 32 | https://www.youtube.com/watch?v=Vp-gijKxw1o |
| 33 | https://www.youtube.com/watch?v=RNpNm4shl20 |
| 34 | https://www.youtube.com/watch?v=yqCaiShnfFs |
| 35 | https://www.youtube.com/watch?v=66BlM3tBoBE |
| 36 | https://www.youtube.com/watch?v=oEpL9nF6BO4 |
| 37 | https://www.youtube.com/watch?v=cE7twGhWT_o |
| 38 | https://www.youtube.com/watch?v=50ZHylyb0EA |
| 39 | https://www.youtube.com/watch?v=9w0TAvK875w |
| 40 | https://www.youtube.com/watch?v=UvMZHyCQu3w |
| 41 | https://www.youtube.com/watch?v=uGc03QX8HfI |
| 42 | https://www.youtube.com/watch?v=P_hsDVWQ61o |
| 43 | https://www.youtube.com/watch?v=W5_KjKmCGuM |
| 44 | https://www.youtube.com/watch?v=vEfQzfTWpNM |
| 45 | https://www.youtube.com/watch?v=wphghAKYPvQ |
| 46 | https://www.youtube.com/watch?v=Hdf_PGhf3r4 |
| 47 | https://www.youtube.com/watch?v=9gmfSre6vv4 |
| 48 | https://www.youtube.com/watch?v=oteGphTe1Bc |
| 49 | https://www.youtube.com/watch?v=7taMZZ9sDUg |
| 50 | https://www.youtube.com/watch?v=lNW5Wzkw6OI |
| 51 | https://www.youtube.com/watch?v=fFYUmKwVRFM |
| 52 | https://www.youtube.com/watch?v=b_eaK5jkQ8E |
| 53 | https://www.youtube.com/watch?v=GjcmnBzrgrI |
| 54 | https://www.youtube.com/watch?v=B0qsMMk-58Q |
| 55 | https://www.youtube.com/watch?v=v9sri2IqYWU |

#### 4. MATHU MATTHU BARAHADA NADUVINA GONDALA (ಮಾತು ಮತ್ತು ಬರಹದ ನಡುವಿನ ಗೊಂದಲ) - 44 parts

| # | Link |
|---|------|
| 1 | https://www.youtube.com/watch?v=odO4e-zuEGo |
| 2 | https://www.youtube.com/watch?v=k4pLk8-vD3c |
| 3 | https://www.youtube.com/watch?v=_OEs3bqosv0 |
| 4 | https://www.youtube.com/watch?v=quQjHn3f4no |
| 5 | https://www.youtube.com/watch?v=UTN6gE3JPss |
| 6 | https://www.youtube.com/watch?v=xdlMTV5Srkg |
| 7 | https://www.youtube.com/watch?v=J8Yv4kj2Nkc |
| 8 | https://www.youtube.com/watch?v=XZDXoAg_4-U |
| 9 | https://www.youtube.com/watch?v=hZKm7LidDw8 |
| 10 | https://www.youtube.com/watch?v=jNwK9yyNGUk |
| 11 | https://www.youtube.com/watch?v=9KH3llP3pqE |
| 12 | https://www.youtube.com/watch?v=ll0vGK6YlWA |
| 13 | https://www.youtube.com/watch?v=BKa4yjPccns |
| 14 | https://www.youtube.com/watch?v=4JYucob2tdc |
| 16 | https://www.youtube.com/watch?v=_fAY66UpQB4 |
| 17 | https://www.youtube.com/watch?v=-t2gfHFfnU8 |
| 18 | https://www.youtube.com/watch?v=FrbxrT1cfQI |
| 19 | https://www.youtube.com/watch?v=gO2SjO6aU8M |
| 20 | https://www.youtube.com/watch?v=8PWd-Qp7dTw |
| 21 | https://www.youtube.com/watch?v=wVCMDxaZ5Gw |
| 22 | https://www.youtube.com/watch?v=mDBxUKZk-ZM |
| 23 | https://www.youtube.com/watch?v=__pYhDK5m_M |
| 24 | https://www.youtube.com/watch?v=zf3h85nR378 |
| 25 | https://www.youtube.com/watch?v=2Wqx2FoKx1w |
| 26 | https://www.youtube.com/watch?v=r6Bh6Vaj77w |
| 27 | https://www.youtube.com/watch?v=WQ2DiwxKpZA |
| 28 | https://www.youtube.com/watch?v=dQNptM9yK2s |
| 29 | https://www.youtube.com/watch?v=b8bE1gH2oFE |
| 30 | https://www.youtube.com/watch?v=k5a95b_zTKk |
| 31 | https://www.youtube.com/watch?v=wUGetEvg9Jo |
| 32 | https://www.youtube.com/watch?v=p_7tWe3s44g |
| 34 | https://www.youtube.com/watch?v=GqJZTMtfN1k |
| 36 | https://www.youtube.com/watch?v=nAVswfPEHN0 |
| 37 | https://www.youtube.com/watch?v=D-WBsjYvr5M |
| 38 | https://www.youtube.com/watch?v=2vicIvkeCec |
| 39 | https://www.youtube.com/watch?v=93WvwNQZHNs |
| 40 | https://www.youtube.com/watch?v=8K6NHQ1qfZg |
| 41 | https://www.youtube.com/watch?v=aAj7iBYHXCQ |
| 42 | https://www.youtube.com/watch?v=PK6Cp51Vjos |
| 43 | https://www.youtube.com/watch?v=O1DyIlZO6nw |
| 44 | https://www.youtube.com/watch?v=f91qwRec_Ho |

#### 5. MATHINA OLAGUTTU (ಮಾತಿನ ಒಳಗುಟ್ಟು) - 37 parts

| # | Link |
|---|------|
| 1 | https://www.youtube.com/watch?v=4j-3ROIe4tc |
| 2 | https://www.youtube.com/watch?v=beZuO8bdj8Y |
| 3 | https://www.youtube.com/watch?v=rFM-0Jtmios |
| 4 | https://www.youtube.com/watch?v=tkVwJqoV6k4 |
| 5 | https://www.youtube.com/watch?v=080sXdaVmWI |
| 6 | https://www.youtube.com/watch?v=rKIqznWqKUI |
| 7 | https://www.youtube.com/watch?v=HIYFOJt4jKs |
| 8 | https://www.youtube.com/watch?v=BL8nQ-wgh8s |
| 9 | https://www.youtube.com/watch?v=POoyFWpUvic |
| 10 | https://www.youtube.com/watch?v=eEHUpowQLAo |
| 11 | https://www.youtube.com/watch?v=DmUtVIhr_5Q |
| 12 | https://www.youtube.com/watch?v=Dmah0NmF5y4 |
| 13 | https://www.youtube.com/watch?v=Ip7K0_0jedA |
| 14 | https://www.youtube.com/watch?v=YwxRXyKUQFI |
| 15 | https://www.youtube.com/watch?v=Plk0dYJrzJA |
| 16 | https://www.youtube.com/watch?v=ylWd_oN4BYE |
| 17 | https://www.youtube.com/watch?v=fImAEJ7IptE |
| 18 | https://www.youtube.com/watch?v=TNh9suG85LU |
| 19 | https://www.youtube.com/watch?v=-zw1bQJhrhQ |
| 20 | https://www.youtube.com/watch?v=A7FUifvLA6k |
| 21 | https://www.youtube.com/watch?v=qRpWjKJhJVU |
| 22 | https://www.youtube.com/watch?v=528w_-IgdHI |
| 23 | https://www.youtube.com/watch?v=oSZ5MZEDgO0 |
| 24 | https://www.youtube.com/watch?v=brzUWBq6yao |
| 25 | https://www.youtube.com/watch?v=ToLPdT1n3jE |
| 26 | https://www.youtube.com/watch?v=hMaYkchkMWo |
| 27 | https://www.youtube.com/watch?v=iq4d9H2vKFg |
| 28 | https://www.youtube.com/watch?v=2za2DSf2iHs |
| 29 | https://www.youtube.com/watch?v=FSsnMU8qptc |
| 30 | https://www.youtube.com/watch?v=m6dVCrTgxxE |
| 31 | https://www.youtube.com/watch?v=-Bf8ujA6ETY |
| 32 | https://www.youtube.com/watch?v=_ZX3f-jSkHg |
| 33 | https://www.youtube.com/watch?v=kmrFW5ARQok |
| 34 | https://www.youtube.com/watch?v=8qlznZyV500 |
| 35 | https://www.youtube.com/watch?v=HDyjoRXzlcQ |
| 36 | https://www.youtube.com/watch?v=EsCnHBheG1A |
| 37 | https://www.youtube.com/watch?v=0yatMpLIWJI |

#### 6. KALIKENUDI MATTHU NUDIKALIKE (ಕಲಿಕೆನುಡಿ ಮತ್ತು ನುಡಿಕಲಿಕೆ) - 21 parts

| # | Link |
|---|------|
| P1 | https://www.youtube.com/watch?v=qjrMOYew6UE |
| P2 | https://www.youtube.com/watch?v=enhh0H-Rt4s |
| 1 | https://www.youtube.com/watch?v=mclGOqYupR4 |
| 2 | https://www.youtube.com/watch?v=rDm3X5ZWpRc |
| 3 | https://www.youtube.com/watch?v=T-A3CjbxCWY |
| 4 | https://www.youtube.com/watch?v=g_RBjxmF5gw |
| 5 | https://www.youtube.com/watch?v=Lx3KxNn5WW4 |
| 6 | https://www.youtube.com/watch?v=QsFV_yIRn-w |
| 7 | https://www.youtube.com/watch?v=TjtcJkQlhGY |
| 8 | https://www.youtube.com/watch?v=7A7atZR1BfQ |
| 9 | https://www.youtube.com/watch?v=H4_SQg-rc18 |
| 10 | https://www.youtube.com/watch?v=JDxUQBb0ACg |
| 11 | https://www.youtube.com/watch?v=-8dFeUUZ2_o |
| 12 | https://www.youtube.com/watch?v=-T09dkqV6KE |
| 13 | https://www.youtube.com/watch?v=MgvDbmyYvM4 |
| 14 | https://www.youtube.com/watch?v=WsC8OqKO8sY |
| 15 | https://www.youtube.com/watch?v=HRX_xCTZpaI |
| 16 | https://www.youtube.com/watch?v=wy63HbHd0As |
| 17 | https://www.youtube.com/watch?v=kH7s2LDPFjo |
| 18 | https://www.youtube.com/watch?v=TA5PRus2K7Q |
| 19 | https://www.youtube.com/watch?v=mFZbqdhuEbg |

#### 7. KANNADADA SOLLARIME (ಕನ್ನಡದ ಸೊಲ್ಲರಿಮೆ) - 23 parts

| # | Link |
|---|------|
| P1 | https://www.youtube.com/watch?v=hwh6dmn5NJM |
| P2 | https://www.youtube.com/watch?v=t2tvZ0d9To8 |
| 1 | https://www.youtube.com/watch?v=HFLrH6eg49I |
| 2 | https://www.youtube.com/watch?v=E7Rvg4XgpW8 |
| 3 | https://www.youtube.com/watch?v=Uj3Lfg0JpFc |
| 4 | https://www.youtube.com/watch?v=NKbcmr2GQQQ |
| 5 | https://www.youtube.com/watch?v=PFviQ-mm4Gw |
| 6 | https://www.youtube.com/watch?v=MKfCYjlbr5o |
| 7 | https://www.youtube.com/watch?v=4gVW_iMtKgs |
| 8 | https://www.youtube.com/watch?v=YLWEwp5mN3s |
| 9 | https://www.youtube.com/watch?v=UC8FbIUjPoA |
| 10 | https://www.youtube.com/watch?v=4TdAjUNCT-Q |
| 11 | https://www.youtube.com/watch?v=H5iY_dPH4YU |
| 12 | https://www.youtube.com/watch?v=jZ1w0f9pleU |
| 13 | https://www.youtube.com/watch?v=bwDvWCuZfH0 |
| 14 | https://www.youtube.com/watch?v=f1OnB7cd7UA |
| 15 | https://www.youtube.com/watch?v=DZ_6ic6zZzc |
| 16 | https://www.youtube.com/watch?v=Z7u0JAW43Rc |
| 17 | https://www.youtube.com/watch?v=4Ik-Uj_LDUo |
| 18 | https://www.youtube.com/watch?v=6MtCQBk6o_c |
| 19 | https://www.youtube.com/watch?v=9hQ9knfzTKs |
| 20 | https://www.youtube.com/watch?v=eMSIqhl-MkY |
| 21 | https://www.youtube.com/watch?v=v-TAxQLwbpc |

#### 8. KANNADAKKE MAHAPRANA YAKE BEDA (ಕನ್ನಡಕ್ಕೆ ಮಹಾಪ್ರಾಣ ಯಾಕೆ ಬೇಡ) - 19 parts

| # | Link |
|---|------|
| P1 | https://www.youtube.com/watch?v=JRhErUXyoZk |
| P2 | https://www.youtube.com/watch?v=O_VLpe_aHeU |
| 1 | https://www.youtube.com/watch?v=_yywGdjvPHQ |
| 2 | https://www.youtube.com/watch?v=rjQKR_NJgKM |
| 3 | https://www.youtube.com/watch?v=ZCeqhooYVoQ |
| 4 | https://www.youtube.com/watch?v=zy1RgBHaILs |
| 5 | https://www.youtube.com/watch?v=PpXhpYEnPDo |
| 6 | https://www.youtube.com/watch?v=Ea6W1QIr3NQ |
| 7 | https://www.youtube.com/watch?v=dYHi4eGD39M |
| 8 | https://www.youtube.com/watch?v=aXjOIhOKnfw |
| 9 | https://www.youtube.com/watch?v=4ERWE_gKRTI |
| 10 | https://www.youtube.com/watch?v=MdcQouKBmj0 |
| 11 | https://www.youtube.com/watch?v=dABNPe9wCSE |
| 12 | https://www.youtube.com/watch?v=z9S9O4ajuzY |
| 13 | https://www.youtube.com/watch?v=rdJquejIyM0 |
| 14 | https://www.youtube.com/watch?v=Aq_k6LMKo-I |
| 15 | https://www.youtube.com/watch?v=M_nULm0oUzk |
| 16 | https://www.youtube.com/watch?v=W6y11I85CIU |
| 17 | https://www.youtube.com/watch?v=808vV-3N33g |

#### 9. HAVYAKA KANNADA (ಹವ್ಯಕ ಕನ್ನಡ) - 43 parts

| # | Link |
|---|------|
| P1 | https://www.youtube.com/watch?v=E7HaY1nm9bE |
| P2 | https://www.youtube.com/watch?v=KJojbqhJPIo |
| P3 | https://www.youtube.com/watch?v=t4prq5X0aqQ |
| P4 | https://www.youtube.com/watch?v=P3EGNh2lATY |
| P5 | https://www.youtube.com/watch?v=e0nnfbmaclU |
| P6 | https://www.youtube.com/watch?v=xajOV0duF5s |
| 1 | https://www.youtube.com/watch?v=4-2JbFQkX9Y |
| 2 | https://www.youtube.com/watch?v=MvQbfj0CkkA |
| 3 | https://www.youtube.com/watch?v=ffZNlckWkEw |
| 4 | https://www.youtube.com/watch?v=77Jm5TrnwNE |
| 5 | https://www.youtube.com/watch?v=sdbtXnPMhzU |
| 6 | https://www.youtube.com/watch?v=nqEh1yuVYu0 |
| 7 | https://www.youtube.com/watch?v=wop-G0a32K8 |
| 8 | https://www.youtube.com/watch?v=Jyv7RAWiHjQ |
| 9 | https://www.youtube.com/watch?v=S0A77BnDWE4 |
| 10 | https://www.youtube.com/watch?v=waBrKRbyzI4 |
| 11 | https://www.youtube.com/watch?v=HLH3k-WRUGg |
| 12 | https://www.youtube.com/watch?v=4AkjeKd9JSk |
| 13 | https://www.youtube.com/watch?v=9JOjIxq_yj4 |
| 14 | https://www.youtube.com/watch?v=18oUDlQMdHA |
| 15 | https://www.youtube.com/watch?v=T_RFS2HcwQw |
| 16 | https://www.youtube.com/watch?v=BcVE_GcqEW8 |
| 17 | https://www.youtube.com/watch?v=2mNoeon0dms |
| 18 | https://www.youtube.com/watch?v=pXAGhNZmDOI |
| 19 | https://www.youtube.com/watch?v=0fWqSfYky1Y |
| 20 | https://www.youtube.com/watch?v=zQYzJbZSnv0 |
| 21 | https://www.youtube.com/watch?v=uYKLxvIawfw |
| 22 | https://www.youtube.com/watch?v=QuW2BO1S4YE |
| 23 | https://www.youtube.com/watch?v=IkYuQ5WjK2k |
| 24 | https://www.youtube.com/watch?v=ZIlOj80TLhw |
| 25 | https://www.youtube.com/watch?v=wrCUhpVCiys |
| 26 | https://www.youtube.com/watch?v=wnqNXVe_lXU |
| 27 | https://www.youtube.com/watch?v=OrjRVjDDdjg |
| 28 | https://www.youtube.com/watch?v=KlWkQeT0k04 |
| 29 | https://www.youtube.com/watch?v=xLrdeg3kPUA |
| 30 | https://www.youtube.com/watch?v=7kyLbh_uM6s |
| 31 | https://www.youtube.com/watch?v=tjifKHk8GsU |
| 32 | https://www.youtube.com/watch?v=W3qaIEHlaWQ |
| 33 | https://www.youtube.com/watch?v=v-UJyKV7jzY |
| 34 | https://www.youtube.com/watch?v=iUU3QdUMyck |
| 35 | https://www.youtube.com/watch?v=Txjirqdx--s |
| 36 | https://www.youtube.com/watch?v=hExoKikHKzQ |
| 37 | https://www.youtube.com/watch?v=RSFfRv6l-58 |

#### 10. KANNADA NUDIYA HINNADAVALI (ಕನ್ನಡ ನುಡಿಯ ಹಿನ್ನಡವಳಿ) - 14 parts

| # | Link |
|---|------|
| P1 | https://www.youtube.com/watch?v=Lo04bvzvxCY |
| P2 | https://www.youtube.com/watch?v=-g6_cosSsJI |
| 1 | https://www.youtube.com/watch?v=JIrRZ1X2hoE |
| 2 | https://www.youtube.com/watch?v=bgn3L2rtDfk |
| 4 | https://www.youtube.com/watch?v=yIkkElp6CfY |
| 5 | https://www.youtube.com/watch?v=uRaGy4ZTeKI |
| 6 | https://www.youtube.com/watch?v=OmZJtoyHiA4 |
| 7 | https://www.youtube.com/watch?v=cFoeWBM3RNY |
| 8 | https://www.youtube.com/watch?v=njJKI8_XFhE |
| 9 | https://www.youtube.com/watch?v=sZ0UDXXPfDo |
| 10 | https://www.youtube.com/watch?v=Z6sE_5ZNCYg |
| 11 | https://www.youtube.com/watch?v=ZrFEgzKrPiQ |
| 12 | https://www.youtube.com/watch?v=EY35YdFlK-s |

#### 11. KANNADA BARAHADA PADASAMASYE (ಕನ್ನಡ ಬರಹದ ಪದಸಮಸ್ಯೆ) - 25 parts

| # | Link |
|---|------|
| 1 | https://www.youtube.com/watch?v=lkx-LmOhI6I |
| 2 | https://www.youtube.com/watch?v=aK1CRXoBTlE |
| 3 | https://www.youtube.com/watch?v=597P4tU0h40 |
| 4 | https://www.youtube.com/watch?v=xP6WmqsqGzs |
| 5 | https://www.youtube.com/watch?v=g5m0hguKACU |
| 6 | https://www.youtube.com/watch?v=mCN6yLbt9-Q |
| 7 | https://www.youtube.com/watch?v=BCPfiTsUvmA |
| 8 | https://www.youtube.com/watch?v=NpsS0ZSx7II |
| 9 | https://www.youtube.com/watch?v=CQYMk6PB3uA |
| 10 | https://www.youtube.com/watch?v=sVJH-Dom5bY |
| 11 | https://www.youtube.com/watch?v=1eC_B1cizv0 |
| 12 | https://www.youtube.com/watch?v=uCkKbncJyuo |
| 13 | https://www.youtube.com/watch?v=zy-xGxBRZSc |
| 14 | https://www.youtube.com/watch?v=2SyjtbOrdQs |
| 15 | https://www.youtube.com/watch?v=9oolaEaFFkw |
| 16 | https://www.youtube.com/watch?v=raiT6C_6DW0 |
| 17 | https://www.youtube.com/watch?v=4W8nzMdPjeg |
| 18 | https://www.youtube.com/watch?v=a0xUwIZGzAk |
| 19 | https://www.youtube.com/watch?v=E1B_gyAhDOc |
| 20 | https://www.youtube.com/watch?v=krNQIH2GQlo |
| 21 | https://www.youtube.com/watch?v=aReQJ5_L2wA |
| 22 | https://www.youtube.com/watch?v=vG70TIoGink |
| 23 | https://www.youtube.com/watch?v=-vPeBijXr1Y |
| 24 | https://www.youtube.com/watch?v=bn3KCtLtXq0 |
| 25 | https://www.youtube.com/watch?v=2uPu36Unvwc |

#### 12. KANNADA BHASHEYA KALPITA CHARITRE (ಕನ್ನಡ ಭಾಷೆಯ ಕಲ್ಪಿತ ಚರಿತ್ರೆ) - 2 parts

| # | Link |
|---|------|
| 1 | https://www.youtube.com/watch?v=soIzNPvrYRw |
| 2 | https://www.youtube.com/watch?v=T75Y9U8lYn8 |

#### 13. DHAREGE DODDAVARU (by Meti Mallikarjun) - 4 parts

| # | Link |
|---|------|
| 1 | https://www.youtube.com/watch?v=1lcY3XgtfTA |
| 2 | https://www.youtube.com/watch?v=HcdPAKeSGvI |
| 3 | https://www.youtube.com/watch?v=njQ_wuVn3Cw |
| 4 | https://www.youtube.com/watch?v=Lm4Do-3zjTY |

### Standalone Videos about DNS Bhat

| Video | Link |
|-------|------|
| DNS BHAT : First Interview - Part 1 | https://www.youtube.com/watch?v=HMXoCD9eVL8 |
| DNS BHAT : First Interview - Part 2 | https://www.youtube.com/watch?v=y8R2-ukhGIk |
| DNS BHAT : First Interview - Part 3 | https://www.youtube.com/watch?v=_Ju3mqPmdtc |
| DNS BHAT : First Interview - Part 4 | https://www.youtube.com/watch?v=YTBOC7cJ5sY |
| DNS BHAT BOOKS | https://www.youtube.com/watch?v=YYfbva1Nzcc |
| Prof. DNS BHAT "Read my books..." | https://www.youtube.com/watch?v=61U-a5PFmts |
| DNS BHAT interview by AKSHARA of NINASAM | https://www.youtube.com/watch?v=afcPBX29gEw |
| DNS BHAT explains why 31 letters are enough | https://www.youtube.com/watch?v=Qt9HkiCJvgg |
| HOSA BARAHA (new writing) FOR KANNADA | https://www.youtube.com/watch?v=peyZ27kwOko |
| BOOK RELEASE: KANNADA BARAHADA PADASAMASYE | https://www.youtube.com/watch?v=DhuHtWtsdQU |
| Shambha Joshi award to Dr.D.N.S.Bhat | https://www.youtube.com/watch?v=W2j7-OkbyTQ |

---

## User

print this chat

## Assistant

Offered three options:
1. Select all text in VS Code chat panel (Cmd+A, Cmd+C)
2. Screenshot (Cmd+Shift+3 or Cmd+Shift+4)
3. Save the table contents to a file

## User

(Selected option 3)

## Assistant

Wrote the video listing to `malatibhat_dns_bhat_videos.md`.

## User

Can you write this chat window as a .md file as well?

## Assistant

Wrote this file: `malatibhat_dns_bhat_chat.md`.
