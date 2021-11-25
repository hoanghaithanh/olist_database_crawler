

<!-- ABOUT THE PROJECT -->
## About The Project

Brazilian E-Commerce Public Dataset by Olist crawler.

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

This project requires following packages/modules:

* python3
  ```sh
  sudo apt-get install python3.9
  ```


### Installation


1. Generate a Kaggle API credential json file as guided in [https://www.kaggle.com/docs/api](https://www.kaggle.com/docs/api)
2. Clone the repo
   ```sh
   git clone https://github.com/hoanghaithanh/olist_database_crawler.git
   ```
3. Install vitual enviroment
   ```sh
   cd olist_database_crawler
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. Setup config folder for kaggle
   ```sh
   export KAGGLE_CONFIG_DIR=[fullpath/to/secret/folder]
   ```
5. Copy json file downloaded from step 1 to secret folder
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

### Manually trigger the crawler
```sh
  cd [path/to/root/folder]
  source venv/bin/activate
  python main.py
  ```
### Setup cron job

1. Change [path/to/root/folder] path to actual root folder path in olist_database_crawler file
2. Default cron schedule is set to @daily at 0AM (0 * * * *), change it as you desire.
3. Copy olist_database_crawler file to /etc/cron.d/ folder
<p align="right">(<a href="#top">back to top</a>)</p>

## Giải thích cách làm

1. Về database schema

    Do giới hạn về thời gian (2 tiếng), project này sử dụng schema ban đầu của database Brazilian E-Commerce Public Dataset
![Database Schema](https://i.imgur.com/HRhd2Y0.png)

2. Về công nghệ sử dụng

    Để có thể demo trong thời gian ngắn, project sử dụng cron job đề xếp lịch cho task và sử dụng sqlite để lưu trữ dữ liệu.