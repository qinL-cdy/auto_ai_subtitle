# auto ai subtitle translator

## 0909更新
新增指定whisper model功能，支持使用huggingface下载的自定义model

## 简介
ai字幕生成，字幕翻译 基于openai/whisper、translate、ffmpeg，自动为视频生成翻译过后的srt字幕文件，支持自定义各种语言

## 功能
1.基于视频中的语音直接生成字幕文件  
2.翻译字幕文件

## 使用方法
安装 `ffmpeg`

安装依赖 `pip install -r requirements.txt`

将配置信息填入 `config.yaml`

执行 `python main.py`

## 效果
原视频：

![img.png](img.png)

执行脚本后生成以下文件：

![img_2.png](img_2.png)

添加生成的字幕文件后：

![img_1.png](img_1.png)
