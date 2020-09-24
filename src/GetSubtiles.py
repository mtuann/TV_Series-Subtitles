import os
import glob
import requests
from bs4 import BeautifulSoup
import bs4
import json

def unZipFile(path_folder=""):
    files = glob.glob(os.path.join(path_folder, "**", "*.zip"), recursive=True)
    # print(files)
    for idx, file in enumerate(files):
        cmd_unzip = "unzip {} -d {}".format(file, path_folder + "/subtitles")
        os.system(cmd_unzip)
        print("DONE unzip:", idx + 1, file)
        
# unZipFile("/media/tuan/DATA/TuanNM/TVSerires-Scripts/TV_series_subtitles/t70s")

# unZipFile("/media/tuan/DATA/TuanNM/TVSerires-Scripts/TV_series_subtitles/2aahm")
# unZipFile("/media/tuan/DATA/TuanNM/TVSerires-Scripts/TV_series_subtitles/ILoveLucy")



def get_data_url(url):
#     url = "https://transcripts.foreverdreaming.org/viewforum.php?f=177\&start={}"
#     print("url: {}".format(url))

    while True:
        try : 
            req = requests.get(url)            
            soup = BeautifulSoup(req.text, features="html.parser")
            if (len(soup.text)) > 100:
                break
        except:
            pass
    return soup


def readDataJSONFile(json_path):
    return json.load(open(json_path, "r"))

def writeToJSONFile(data, json_path):
    json.dump(data, open(json_path, "w"), indent=2)
    print("DONE write to file: {}".format(json_path))


def getListFile(folder_path="", pattern="*.srt"):
    return sorted(glob.glob(os.path.join(folder_path, "**", pattern), recursive=True))

class GetSubtitlesFromSRT():
    # Malcolm in the middle
    def __init__(self, folder_srt="/media/tuan/DATA/TuanNM/TVSerires-Scripts/TV_series_subtitles/mitm/subtitles"):
        pass

        # self.files_srt = getListFile(folder_srt)

        # self.readDataSRTFile(self.files_srt[0])

        # self.getEpisodeMalcolmInTheMiddle("/media/tuan/DATA/TuanNM/TVSerires-Scripts/TV_series_subtitles/mitm/subtitles")
        # self.getEpisodeILoveLucy("/media/tuan/DATA/TuanNM/TVSerires-Scripts/TV_series_subtitles/ILoveLucy/subtitles")
        self.getEpisode2aahm("/media/tuan/DATA/TuanNM/TVSerires-Scripts/old/TV_series_subtitles/2aahm/subtitles")

        # self.getEpisodeThat70sShow("/media/tuan/hdd02/TV_series-Subtiles/TV_series_subtitles/t70s/subtitles")

    def getEpisodeThat70sShow(self, folder_path_srt):

        all_data = {}

        files_srt = getListFile(folder_path_srt)

        for idx, value in enumerate(files_srt):
            if idx % 10 == 0:
                print("Reading to {} / {}".format(idx + 1, len(files_srt)))
            title = value.split("/")[-1].replace(".srt", "").replace(" - ", " ")



            data = self.readDataSRTFileT70S(value)
            all_data[title] = data
        #     break
        # return
        

        all_data = sorted(all_data.items(), key=lambda kv : kv[0])

        results = {}

        for idx, k in enumerate(all_data):
            # print(idx, k[0])
            results[k[0]] = k[1]

        print("#NumFile: {}".format(len(results)))

        writeToJSONFile(results, "./t70s_scripts.json")



    def getEpisode2aahm(self, folder_path_srt):
        season_09_titles = "Nice to Meet You, Walden Schmidt (1)|\
People Who Love Peepholes (2)|\
Big Girls Don't Throw Food|\
Nine Magic Fingers|\
A Giant Cat Holding a Churro|\
The Squat and The Hover|\
Those Fancy Japanese Toilets|\
Thank You For The Intercourse|\
Frodo's Headshots|\
A Fishbowl Full of Glass Eyes|\
What a Lovely Landing Strip|\
One False Move, Zimbabwe!|\
Slowly and in a Circular Fashion|\
A Possum on Chemo|\
The Duchess of Dull-In-Sack|\
Sips, Sonnets And Sodomy|\
Not In My Mouth|\
The War Against Gingivitis|\
Palmdale, Ech|\
Grandma's Pie|\
Mr. Hose Says 'Yes'|\
Why We Gave Up Women|\
The Straw In My Donut Hole|\
Oh Look! Al-Qaeda!|".split("|")
        # print(season_09_titles, len(season_09_titles))
        # return
        all_data = {}
        data_season = {}

        files_srt = getListFile(folder_path_srt)

        for idx, value in enumerate(files_srt):
            if idx % 10 == 0:
                print("Reading to {} / {}".format(idx + 1, len(files_srt)))

            if "Two.and.a.Half.Men" in value:

                if "S09" in value:

                    title = value.split("/")[-1]
                    episode = title[:len("Two.and.a.Half.Men.S11E02")].replace(".", " ")
                    title = f'{episode} {season_09_titles[int(episode[-2:]) - 1]}'
                    # print(idx, title)


                else:

                    # print(idx, value)
                    title = value.split("/")[-1]
                    title = title.split(".1080p.")[0]

                    episode = title[:len("Two.and.a.Half.Men.S11E02")].replace(".", " ")
                    title = title[len("Two.and.a.Half.Men.S11E02")+1:].replace(".", " ")

                    # print(idx, episode, title)
                    title = "{} {}".format(episode, title)
                    # print(idx, title)


            elif "Two and a Half Men - 05" in value:
                title = value.split("/")[-1]
               
                
                episode = title.split(" - ")[-2].strip()

                episode = f'S{episode[:2]}E{episode[3:5]}'

                title = title.split(" - ")[-1].strip().split(".en.srt")[0].strip()
                # print(idx, episode, title)
                title = "Two and a Half Men {} {}".format(episode, title)
                # print(idx, title)
                # pass
            else:
                title = value.split("/")[-1].split(" 1080p ")[0]

            

            # print(idx, title)

            season = title[:len("Two and a Half Men S10")][-3:]

            # print(idx, title, season)
            if season not in data_season:
                data_season[season] = 0
            data_season[season] += 1

                # pass

                # value = "06.27 The Ricardos Dedicate A Statue (1957)"
                # episode = value.split("/")[-1][:5]
                # title = value.split("/")[-1].split(".srt")[0][6:]
                # # print(idx, value, title)
                # episode = "S{}E{}".format(episode[:2], episode[3:5])
                # title = "I Love Lucy {} {}".format(episode, title)
                # print(idx, title)

            data = self.readDataSRTFile(value)

            all_data[title] = data

        # print(data_season.sort())
        all_episode = 0

        for k, v in data_season.items():
            print(k, v)
            all_episode += v
        print("#episode:", all_episode)
        
        

            # break
        # orders.items(), key=

        all_data = sorted(all_data.items(), key=lambda kv : kv[0])

        results = {}

        for idx, k in enumerate(all_data):
            # print(idx, k[0])
            results[k[0]] = k[1]

        print("#NumFile: {}".format(len(results)))

        writeToJSONFile(results, "./2aahm_scripts.json")

    def getEpisodeILoveLucy(self, folder_path_srt):
        all_data = {}

        files_srt = getListFile(folder_path_srt)

        for idx, value in enumerate(files_srt):
            if idx % 10 == 0:
                print("Reading to {} / {}".format(idx + 1, len(files_srt)))

            if "I Love Lucy - 0" in value:
                value1 = value.replace("03x18-", "03x18 -")
                # print(idx, value)
                episode = value1.split(" - ")[-2].strip()
                title = value1.split(" - ")[-1].strip().split(".DVD-Rip")[0].strip()
                # if "03x18" in title:
                #     print(idx, value, episode)
                # print(title)

                episode = "S" + episode.replace("x", "E")
                # episode = "0" + episode
                # print(episode)
                # print(title)
                title = "I Love Lucy {} {}".format(episode, title)
                print(idx, title)
                # if "03x18" in title:
                #     print(idx, value)
                # return

                pass

            else:
                # value = "06.27 The Ricardos Dedicate A Statue (1957)"
                episode = value.split("/")[-1][:5]
                title = value.split("/")[-1].split(".srt")[0][6:]
                # print(idx, value, title)
                episode = "S{}E{}".format(episode[:2], episode[3:5])
                title = "I Love Lucy {} {}".format(episode, title)
                print(idx, title)

            data = self.readDataSRTFile(value)

            all_data[title] = data

            
            # break
        # orders.items(), key=

        all_data = sorted(all_data.items(), key=lambda kv : kv[0])

        results = {}

        for idx, k in enumerate(all_data):
            # print(idx, k[0])
            results[k[0]] = k[1]
        print("#NumFile: {}".format(len(results)))

        writeToJSONFile(results, "./ill_scripts.json")

            # break


    def getEpisodeMalcolmInTheMiddle(self, folder_path_srt):
        all_data = {}

        files_srt = getListFile(folder_path_srt)

        for idx, value in enumerate(files_srt):
            if idx % 10 == 0:
                print("Reading to {} / {}".format(idx + 1, len(files_srt)))
            # print(idx, value)
            # if "Malcolm in the Middle S0" in value:
            #     print(idx, value)
            if "Malcolm in the Middle - " in value:
                # print(idx, value)
                episode = value.split(" - ")[-2].strip()

                title = value.split(" - ")[-1].strip().split(".HDTV")[0].strip()
                # print("---- {} = {}".format(episode, value))
                
                # episode = "6x10".format("%dx%d")
                # print("idx: {} episode: {}".format(idx, episode))
                # print(idx, value, episode)
                title = "Malcolm in the Middle S0{}E{} {}".format(episode[0], episode[2:4], title)
                # print("\tidx: {} title: {}".format(idx + 1, title))

            else:

                title = os.path.basename(value).split(".srt")[0]
                # print("\tidx: {} title: {}".format(idx + 1, title))
                # "%dx%d"


            data = self.readDataSRTFile(value)
            # break
            # print(len(data))

            all_data[title] = data

            
            # break
        # orders.items(), key=

        all_data = sorted(all_data.items(), key=lambda kv : kv[0])

        results = {}

        for idx, k in enumerate(all_data):
            # print(idx, k[0])
            results[k[0]] = k[1]
        writeToJSONFile(results, "./mitm_scripts.json")
        # print(all_data)

            # print

            # if "Malcolm in the Middle - 7x" in value:
            #     continue
                # print(idx, value)


            # break



    def readDataSRTFileT70S(self, file_path):
        print("path_srt: {}".format(file_path))
        # data = open(file_path, 'rU', encoding='windows-1252').read()
        data = open(file_path, 'rU', errors='ignore').read()

        chr_rep = chr(0)
        data = data.replace(chr_rep, "")

        
   
        data = data.split(" --> ")
        # print(len(data))


        # return None

        
        # print(len(data), data[0], data[1])
        # return None

        # print(data[1])
        results = []
        for idx, data1 in enumerate(data):
            # if idx == 5:
            #     break
            if "www.tvsubtitles.net" in data1:
                continue

            # print("----" * 20)

            # print("Start idx: {}".format(idx))
            # print("Raw data: {}".format(data1))


            # # data1 = data1[(len("00:00:03,632") + 1) : -(len("00:00:03,632") + 3)].replace("\n", "")
            
            # # print("DATA1", data1)
            # # print(idx, data1)
            # print("END DATARAW")
            # print("----" * 20)
            

            rindex = data1.rfind("\n\n\n")
            lindex = data1.index("\n\n")
            data1 = data1[lindex + 2 : rindex - 1].replace("\n\n", "\n")

            # print(data1)

            # print("data1", data1)
            data1 = data1.replace("</i>", "")
            data1 = data1.replace("<i>", "")
            data1 = data1.replace("j\& ", "")
            data1 = data1.replace(" j\&", "")
            
            
            

            
            if len(data1) > 0 and idx > 0:
                # print("{}: {}".format(idx, data1))
                # print(data1)
                results.append(data1)

        return results

    def readDataSRTFile(self, file_path):
        # print("path_srt: {}".format(file_path))
        data = open(file_path, 'rU', encoding='windows-1252').read()

        # data = str(open(file_path, "r").read().encode('windows-1252'))

        data = data.split("-->")
        # print(len(data))
        # print(data[1])
        results = []
        for idx, data1 in enumerate(data):
            if "www.tvsubtitles.net" in data1:
                continue

            data1 = data[idx][len("00:00:03,632") + 2:] # .replace("\n\n", "")
            rindex = data1.rfind("\n\n")
            data1 = data1[:rindex]
            # print("data1", data1)
            data1 = data1.replace("</i>", "")
            data1 = data1.replace("<i>", "")

            
            if len(data1) > 0 and idx > 0:
                # print(idx, data1)
                results.append(data1)

        return results


        # print(len(data), data[0], data[len(data) - 1], data[1])

getSubtitlesFromSRT = GetSubtitlesFromSRT()

class DownloadSubtitles():

    # TBBT: 159, 275
    # HIMYM: 177, 200
    def __init__(self, id_tvseries="159", range_url=280):
        self.id_tvseries = id_tvseries
        self.range_url = range_url
        # self.get_list_episode()
        
        # self.data_urls = readDataJSONFile("./tbbt.json")
        # self.get_data_tv_series()

        self.gen_text_subtitles()

    def gen_text_subtitles(self, json_path="./tbbt_scripts.json", txt_path="tbbt_scripts.txt"):
        data = readDataJSONFile(json_path)
        all_text = ""

        for idx, (key, value) in enumerate(data.items()):
            name = key
            subtitle = value["scripts"]
            if len(all_text) > 0:
                all_text += "\n" + name
            else:
                all_text = name

            all_text += "\n" + subtitle
            all_text += "\n" + "***" * 20

        with open(txt_path, "w") as fw:
            fw.write(all_text)

    def get_data_tv_series(self, file_json_write="./tbbt_scripts.json"):
        data = {}

        for idx, (key, value) in enumerate(self.data_urls.items()):
            print("Process to: ", idx+ 1, "/", len(self.data_urls), " --- ", key, value)
            datum = self.get_subtitles_url(value)
            # print(data)
            data[key] = {
                "url" : value,
                "scripts" : datum, 
            }

            # break
        writeToJSONFile(data, file_json_write)

    def get_list_episode(self, file_json_write="./tbbt.json"):
        
        urls = []
        data = {}
        for idx, d in enumerate(range(0, self.range_url, 25)):
            url = "https://transcripts.foreverdreaming.org/viewforum.php?f={}\&start={}".format(self.id_tvseries, d)
            print(idx, url)
            
            soup = get_data_url(url=url)
            # urls +=  
            datum = self.get_urls(soup)
            # print(datum)
            urls += datum
            for dt in datum:
                data[dt[0]] = dt[1]

        print("len urls", len(urls))
        # print(urls)
        writeToJSONFile(data, file_json_write)
        
    def get_urls(self, soup):
        urls = soup.findAll("a")
        ret = []
        for idx, url in enumerate(urls):
            txt = url.text
            if len(txt) > 2 and txt[2] == 'x':
    #             print(idx, url.text)
    #             print(url["href"])
                url_add = "https://transcripts.foreverdreaming.org/" + url["href"][2:-len("\&sid=366c20c84305fe70e06979d3365939d8")]
                ret.append([url.text, url_add ]  )

        return ret

    def get_subtitles_url(self, url):
        soup = get_data_url(url=url)
        ss = soup.findAll('div',  {'class': 'postbody'})
        return ss[0].text.strip()

    def get_subtitles_friends(self):
        soup = get_data_subtitles("https://fangj.github.io/friends/")
        print(len(soup))

    def get_urls_all_friends(self, soup):
        # all_text += "\n" + name + "\n"
        # all_text += get_data_subtitles(url_get).text

        urls = soup.findAll("a")
    #     print(len(urls))
        ret = []
        for idx, url in enumerate(urls):
    #         print(idx, url)
    #         url = url.find('a', href=True)
    #         print(idx, url.text, url.attrs.get("href"))
            txt = url.text
    #         print(txt, url["href"])
            ret.append([url.text, "https://fangj.github.io/friends/" + url["href"]])
        return ret

        urls = get_urls_all_friends(soup)
        print(len(urls))
        print(urls[0])

# downloadSubtitles = DownloadSubtitles()