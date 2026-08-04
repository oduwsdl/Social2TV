# Social2TV

**A Benchmark for Detecting Social Media Content in TV News Archives**

Social2TV is a manually curated multimodal gold-standard dataset for detecting social media references in U.S. cable television news. It covers **36 hours** of prime-time programming from **CNN**, **MSNBC**, and **Fox News** across five dates (one per year, 2020–2024), with labels for:

- **Social media logos** and **post screenshots** visible on TV screen
- **Verbal mentions** of social media in closed captions

The underlying video and caption text remain in the [Internet Archive TV News Archive](https://archive.org/details/tv). This repository releases annotations, timestamps, and episode identifiers that link back to those broadcasts.

---

## Table of Contents

- [Quick links to dataset files](#quick-links-to-dataset-files)
- [Overview](#overview)
- [Repository structure](#repository-structure)
- [Corpus](#corpus)
- [Visual annotations (logos & post screenshots)](#visual-annotations-logos--post-screenshots)
- [Closed-caption annotations](#closed-caption-annotations)
- [Accessing source broadcasts](#accessing-source-broadcasts)
- [Data availability and usage restrictions](#data-availability-and-usage-restrictions)
- [Acknowledgments](#acknowledgments)
- [License](#license)

---

## Quick links to dataset files

### Logos and post screenshots

Positive visual annotations (frames that contain a social media logo and/or a post screenshot):

| Channel | File | Direct download |
|---------|------|-----------------|
| CNN | [`gold_standard_images_cnn.csv`](LogoAndPostScreenshots/gold_standard_images_cnn.csv) | [Download](https://raw.githubusercontent.com/oduwsdl/Social2TV/main/LogoAndPostScreenshots/gold_standard_images_cnn.csv) |
| Fox News | [`gold_standard_images_foxnews.csv`](LogoAndPostScreenshots/gold_standard_images_foxnews.csv) | [Download](https://raw.githubusercontent.com/oduwsdl/Social2TV/main/LogoAndPostScreenshots/gold_standard_images_foxnews.csv) |
| MSNBC | [`gold_standard_images_msnbc.csv`](LogoAndPostScreenshots/gold_standard_images_msnbc.csv) | [Download](https://raw.githubusercontent.com/oduwsdl/Social2TV/main/LogoAndPostScreenshots/gold_standard_images_msnbc.csv) |

Folder: [`LogoAndPostScreenshots/`](LogoAndPostScreenshots/)

### Closed captions

Gold-standard labels for every caption segment (without redistributing caption text):

| Channel | File | Direct download |
|---------|------|-----------------|
| CNN | [`gold_standard_cc_cnn.csv`](ClosedCaptions/gold_standard_cc_cnn.csv) | [Download](https://raw.githubusercontent.com/oduwsdl/Social2TV/main/ClosedCaptions/gold_standard_cc_cnn.csv) |
| Fox News | [`gold_standard_cc_foxnews.csv`](ClosedCaptions/gold_standard_cc_foxnews.csv) | [Download](https://raw.githubusercontent.com/oduwsdl/Social2TV/main/ClosedCaptions/gold_standard_cc_foxnews.csv) |
| MSNBC | [`gold_standard_cc_msnbc.csv`](ClosedCaptions/gold_standard_cc_msnbc.csv) | [Download](https://raw.githubusercontent.com/oduwsdl/Social2TV/main/ClosedCaptions/gold_standard_cc_msnbc.csv) |

Folder: [`ClosedCaptions/`](ClosedCaptions/)

---

## Overview

Social media content frequently appears in television news through platform logos, post screenshots, and verbal references, extending its reach beyond the original platform. These moments typically occupy only a small fraction of airtime, yet they matter because they show when posts, platforms, and online activity are selected, contextualized, and amplified for TV audiences.

Social2TV addresses the lack of a shared evaluation resource for this sparse, multimodal phenomenon. Beyond the benchmark itself, it demonstrates a reusable workflow for enriching television archives with searchable, research-ready metadata.

**Contributions**

1. A multimodal gold standard covering 36 hours of CNN, MSNBC, and Fox News from five selected dates (2020–2024).
2. An extensible annotation workflow adaptable to new dates, channels, platforms, countries, and research domains.
3. Open evaluation resources for detecting visual and caption-based social media references (see [Related code](#related-code)).

---

## Repository structure

```
Social2TV/
├── LogoAndPostScreenshots/          # Visual gold standard (logos + post screenshots)
│   ├── gold_standard_images_cnn.csv
│   ├── gold_standard_images_foxnews.csv
│   └── gold_standard_images_msnbc.csv
├── ClosedCaptions/                  # Closed-caption gold standard (no caption text)
│   ├── gold_standard_cc_cnn.csv
│   ├── gold_standard_cc_foxnews.csv
│   └── gold_standard_cc_msnbc.csv
└── LICENSE
```

---

## Corpus

| Property | Value |
|----------|-------|
| Networks | CNN, Fox News, MSNBC |
| Window | U.S. prime time, 8:00–11:00 p.m. Eastern Time |
| Selected dates (ET) | 2020-03-13, 2021-01-09, 2022-04-24, 2023-01-21, 2024-01-31 |
| Episodes | 36 one-hour news programs (15 Fox News, 12 MSNBC, 9 CNN) |
| Frames reviewed | ~130,000 one-second frames |
| Visual positives released | 1,445 annotated frames with logo and/or screenshot |
| Caption segments | 59,982 labeled segments |

Dates were chosen via GDELT Television Explorer peak-mention searches to enrich for social media references. **Social2TV is a positive-enriched benchmark** for developing and evaluating detectors—not a probability sample for estimating overall prevalence across TV news.

Archive episode IDs use UTC timestamps (prime-time Eastern often falls on the following UTC calendar day). Example: March 13, 2020, 8–9 p.m. ET → `CNNW_20200314_030000_...`.

### Included episodes

<details>
<summary>Fox News (15)</summary>

| Date (ET) | 8–9 PM | 9–10 PM | 10–11 PM |
|-----------|--------|---------|----------|
| 2020-03-13 | [Fox News at Night With Shannon Bream](https://archive.org/details/FOXNEWSW_20200314_030000_Fox_News_at_Night_With_Shannon_Bream) | [Tucker Carlson Tonight](https://archive.org/details/FOXNEWSW_20200314_040000_Tucker_Carlson_Tonight) | [Hannity](https://archive.org/details/FOXNEWSW_20200314_050000_Hannity) |
| 2021-01-09 | [Watters World](https://archive.org/details/FOXNEWSW_20210110_040000_Watters_World) | [Justice With Judge Jeanine](https://archive.org/details/FOXNEWSW_20210110_050000_Justice_With_Judge_Jeanine) | [The Greg Gutfeld Show](https://archive.org/details/FOXNEWSW_20210110_060000_The_Greg_Gutfeld_Show) |
| 2022-04-24 | [Life, Liberty & Levin](https://archive.org/details/FOXNEWSW_20220425_030000_Life_Liberty__Levin) | [The Next Revolution With Steve Hilton](https://archive.org/details/FOXNEWSW_20220425_040000_The_Next_Revolution_With_Steve_Hilton) | [Sunday Night in America With Trey Gowdy](https://archive.org/details/FOXNEWSW_20220425_050000_Sunday_Night_in_America_With_Trey_Gowdy) |
| 2023-01-21 | [One Nation With Brian Kilmeade](https://archive.org/details/FOXNEWSW_20230122_040000_One_Nation_With_Brian_Kilmeade) | [Unfiltered With Dan Bongino](https://archive.org/details/FOXNEWSW_20230122_050000_Unfiltered_With_Dan_Bongino) | [Lawrence Jones Cross Country](https://archive.org/details/FOXNEWSW_20230122_060000_Lawrence_Jones_Cross_Country) |
| 2024-01-31 | [Fox News at Night](https://archive.org/details/FOXNEWSW_20240201_040000_Fox_News_at_Night) | [The Five](https://archive.org/details/FOXNEWSW_20240201_050000_The_Five) | [Jesse Watters Primetime](https://archive.org/details/FOXNEWSW_20240201_060000_Jesse_Watters_Primetime) |

</details>

<details>
<summary>MSNBC (12)</summary>

| Date (ET) | 8–9 PM | 9–10 PM | 10–11 PM |
|-----------|--------|---------|----------|
| 2020-03-13 | [The 11th Hour With Brian Williams](https://archive.org/details/MSNBCW_20200314_030000_The_11th_Hour_With_Brian_Williams) | [The Rachel Maddow Show](https://archive.org/details/MSNBCW_20200314_040000_The_Rachel_Maddow_Show) | [The Last Word With Lawrence O'Donnell](https://archive.org/details/MSNBCW_20200314_050000_The_Last_Word_With_Lawrence_ODonnell) |
| 2021-01-09 | [The Week With Joshua Johnson](https://archive.org/details/MSNBCW_20210110_040000_The_Week_With_Joshua_Johnson) | [The Week With Joshua Johnson](https://archive.org/details/MSNBCW_20210110_050000_The_Week_With_Joshua_Johnson) | — *(Dateline Extra excluded)* |
| 2022-04-24 | [The Mehdi Hasan Show](https://archive.org/details/MSNBCW_20220425_030000_The_Mehdi_Hasan_Show) | [Ayman](https://archive.org/details/MSNBCW_20220425_040000_Ayman) | — *(Dateline excluded)* |
| 2023-01-21 | [American Voices With Alicia Menendez](https://archive.org/details/MSNBCW_20230122_040600_American_Voices_With_Alicia_Menendez) | [Ayman](https://archive.org/details/MSNBCW_20230122_050000_Ayman) | — *(Dateline excluded)* |
| 2024-01-31 | [The 11th Hour With Stephanie Ruhle](https://archive.org/details/MSNBCW_20240201_040000_The_11th_Hour_With_Stephanie_Ruhle) | [Alex Wagner Tonight](https://archive.org/details/MSNBCW_20240201_050000_Alex_Wagner_Tonight) | [The Last Word With Lawrence O'Donnell](https://archive.org/details/MSNBCW_20240201_060000_The_Last_Word_With_Lawrence_ODonnell) |

</details>

<details>
<summary>CNN (9)</summary>

| Date (ET) | 8–9 PM | 9–10 PM | 10–11 PM |
|-----------|--------|---------|----------|
| 2020-03-13 | [CNN Tonight With Don Lemon](https://archive.org/details/CNNW_20200314_030000_CNN_Tonight_With_Don_Lemon) | [Anderson Cooper 360](https://archive.org/details/CNNW_20200314_040000_Anderson_Cooper_360) | [Cuomo Prime Time](https://archive.org/details/CNNW_20200314_050000_Cuomo_Prime_Time) |
| 2021-01-09 | — *(documentary excluded)* | [CNN Newsroom Live](https://archive.org/details/CNNW_20210110_050000_CNN_Newsroom_Live) | [CNN Newsroom Live](https://archive.org/details/CNNW_20210110_060000_CNN_Newsroom_Live) |
| 2022-04-24 | — *(documentary excluded)* | — *(documentary excluded)* | [CNN Newsroom Live](https://archive.org/details/CNNW_20220425_050000_CNN_Newsroom_Live) |
| 2023-01-21 | — *(special excluded)* | — *(special excluded)* | — *(special excluded)* |
| 2024-01-31 | [Laura Coates Live](https://archive.org/details/CNNW_20240201_040000_Laura_Coates_Live) | [Anderson Cooper 360](https://archive.org/details/CNNW_20240201_050000_Anderson_Cooper_360) | [The Source With Kaitlan Collins](https://archive.org/details/CNNW_20240201_060000_The_Source_With_Kaitlan_Collins) |

</details>

Nine documentaries/specials outside regular prime-time news were excluded from the final 36-episode corpus.

---

## Visual annotations (logos & post screenshots)

**Path:** [`LogoAndPostScreenshots/`](LogoAndPostScreenshots/)

Each CSV lists frames that contain at least one visual social media signal (logo and/or post screenshot). Frame files follow:

```text
{episodeID}-{second}.jpg
```

Example: `CNNW_20200314_030000_CNN_Tonight_With_Don_Lemon-000136.jpg` is the frame at second 136 of that episode and (in the gold standard) shows both a Twitter logo and a Twitter post screenshot.

### Schema

| Column | Description |
|--------|-------------|
| `filename` | One-second frame filename (`episodeID-second.jpg`) |
| `Social Media Logo` | `Yes` / `No` — whether a social media platform logo is visible |
| `Social Media Logo Type` | Platform(s) for the logo (e.g., `Twitter`, `TikTok`, `Twitter (X), Instagram`) |
| `Social Media Screenshot` | `Yes` / `No` — whether a social media post screenshot is visible |
| `Social Media Screenshot Type` | Platform(s) for the screenshot (e.g., `Twitter`, `Truth Social`, `No Platform`) |

### Counts (released positive frames)

| Channel | Annotated frames | Logo = Yes | Screenshot = Yes | File |
|---------|------------------|------------|------------------|------|
| CNN | 229 | 154 | 221 | [csv](https://raw.githubusercontent.com/oduwsdl/Social2TV/main/LogoAndPostScreenshots/gold_standard_images_cnn.csv) |
| Fox News | 768 | 728 | 188 | [csv](https://raw.githubusercontent.com/oduwsdl/Social2TV/main/LogoAndPostScreenshots/gold_standard_images_foxnews.csv) |
| MSNBC | 448 | 448 | 282 | [csv](https://raw.githubusercontent.com/oduwsdl/Social2TV/main/LogoAndPostScreenshots/gold_standard_images_msnbc.csv) |
| **Total** | **1,445** | **1,330** | **691** | |

Frames without logos or screenshots are not listed; for full-episode evaluation, treat unlisted seconds in the 36 episodes as negatives.

---

## Closed-caption annotations

**Path:** [`ClosedCaptions/`](ClosedCaptions/)

Each row is one closed-caption segment. **Caption text is not redistributed.** Labels and timing metadata are provided, plus a `clip_url` pointing into the Internet Archive so you can inspect the corresponding audiovisual context.

### Schema

| Column | Description |
|--------|-------------|
| `date` | Broadcast date in the Archive identifier (UTC calendar date) |
| `channel` | `CNN`, `FOXNEWS`, or `MSNBC` |
| `episodeid` | TV News Archive episode identifier |
| `clip_url` | 60-second Archive clip containing the caption midpoint |
| `starttime` / `endtime` | Caption segment times (`HH:MM:SS,mmm`) |
| `starttime_seconds` / `endtime_seconds` | Same bounds in seconds |
| `Social Media Mention` | `Yes` (social media reference), `No`, or `Ad` (commercial break) |
| `Social Media Platform` | Platform(s) mentioned when `Social Media Mention` is `Yes` (e.g., `Twitter`, `Social Media`, `TikTok`) |

### How `clip_url` is constructed

Archive.org serves programs as contiguous 60-second windows (`0–60`, `60–120`, …). For each caption segment with midpoint \(m = (t_{\mathrm{start}} + t_{\mathrm{end}}) / 2\):

```text
https://archive.org/details/{episodeid}/start/{T}/end/{T+60}
```

where \(T = 60 \lfloor m / 60 \rfloor\). Boundary ties prefer the window with greater overlap (earlier window on a remaining tie). Caption clocks can be slightly offset from video; treat `clip_url` as a retrieval pointer, not an exact cut.

Example clip:  
https://archive.org/details/CNNW_20200314_030000_CNN_Tonight_With_Don_Lemon/start/420/end/480

### Counts

| Channel | Segments | Mention = Yes | Mention = Ad | File |
|---------|----------|---------------|--------------|------|
| CNN | 14,764 | 83 | 2,028 | [csv](https://raw.githubusercontent.com/oduwsdl/Social2TV/main/ClosedCaptions/gold_standard_cc_cnn.csv) |
| Fox News | 22,561 | 121 | 3,257 | [csv](https://raw.githubusercontent.com/oduwsdl/Social2TV/main/ClosedCaptions/gold_standard_cc_foxnews.csv) |
| MSNBC | 22,657 | 81 | 4,775 | [csv](https://raw.githubusercontent.com/oduwsdl/Social2TV/main/ClosedCaptions/gold_standard_cc_msnbc.csv) |
| **Total** | **59,982** | **285** | **10,060** | |


---

## Accessing source broadcasts

Social2TV does **not** ship video frames or closed-caption text.

| Need | How |
|------|-----|
| Watch a full episode | `https://archive.org/details/{episodeid}` |
| Watch a time range | `https://archive.org/details/{episodeid}/start/{S}/end/{E}` |
| One-second frames / bulk captions | Contact the Internet Archive (see below) |
| Explore caption mention volume | [GDELT Television Explorer](https://api.gdeltproject.org/api/v2/summary/summary?d=iatv&t=summary) |

For bulk research access beyond the public interface, contact **roger@archive.org** and **info@archive.org** with a description of the proposed research and intended use.

---

### Related code

- Visual detection / multimodal LLM evaluation: [internetarchive/tvnews_socialmedia_mentions](https://github.com/internetarchive/tvnews_socialmedia_mentions) (GSoC 2025)

---

## Data availability and usage restrictions

- Annotations in this repository are released for research use under the [MIT License](LICENSE).
- Television media and closed-caption text are owned by rights holders / the Internet Archive and are **not** redistributed here.
- Use episode IDs, timestamps, and `clip_url` values to retrieve corresponding material from the [TV News Archive](https://archive.org/details/tv).
- Do not treat this positive-enriched set as a prevalence sample of platforms or networks.

---

## Acknowledgments

We thank Roger Macdonald (founder, Internet Archive TV News Archive), Mark Graham (Director, Internet Archive), and Kalev Leetaru (GDELT Project) for supporting this research and facilitating access to Television News Archive data.

---

## License

Annotation files and documentation in this repository are released under the [MIT License](LICENSE). Source television media and closed captions are not included in this release and remain subject to the copyright and usage terms of the Internet Archive.
