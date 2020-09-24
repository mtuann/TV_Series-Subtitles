import json

TemplateOverleaf = "\\documentclass{article}\n\
\\usepackage[utf8]{inputenc}\n\
\\usepackage{hyperref}\n\
\\title{TVSeriesName}\n\
\\author{MINH TUAN NGUYEN --- \href{mailto:tuannm0312@gmail.com}{tuannm0312@gmail.com} }\n\
\\date{September 24, 2020}\n\
\\begin{document}\n\
\\maketitle\n\
\\tableofcontents\n\
{}\n\
\\end{document}"
import re

str_char = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#\$%^\&*()_-+={}[]:;\"'\\|<>?,./"

def removeRedundantChar(s):
    res = ""

    for x in s:
        # print(x)
        if x in str_char:
            res += x
        else:
            res += " "
            # print(x)
    return res
    # return ''.join([x for x in s if x in str_char])



# s = removeRedundantChar("281 - â™ª I'm coming up â™ª\\")
# print(s)
# exit(0)


class GenTextOverleaf():

    def __init__(self):
        # pass
        # self.genTBBT() # 12 seasons, 279 episode
        # self.genSubtitleOverleaf("/media/tuan/DATA/TuanNM/TVSerires-Scripts/Src_data_subtitles/ill_scripts.json", 2, "I Love Lucy", "ILoveLucy") # 181 episodes,
        # self.genSubtitleOverleaf("/media/tuan/DATA/TuanNM/TVSerires-Scripts/Src_data_subtitles/mitm_scripts.json", 4, "Malcolm in the middle", "MalcolmInTheMiddle") # 151 episodes
        self.genSubtitleOverleaf("/media/tuan/DATA/TuanNM/TVSerires-Scripts/Src_data_subtitles/2aahm_scripts.json", 3, "Two and a Half Men", "TwoAndAHalfMen") # 262 episodes
        # self.genSubtitleOverleaf("/media/tuan/DATA/TuanNM/TVSerires-Scripts/Src_data_subtitles/t70s_scripts.json", 4, "That '70s Show", "That70sShow") # 200 episodes



    def genSubtitleOverleaf(self, json_path="./2aahm_scripts.json", splitSeason=3, TVSeriesName="Two and a Half Men", TVShortName="TwoAndAHalfMen"):
        data = json.load(open(json_path, "r"))
        
        print(json_path.split("/")[-1], len(data))
        

        data_sections = {}

        # \section{Season 04}\n\

        # \subsection{Episode 03}\n\

        for idx, (k, v) in enumerate(data.items()):
            # if idx == 110:
            #   break

            season_name = f'{k[:len(f"{TVSeriesName} S12")].replace("S", "Season ")}'

            # print(idx, season_name)
            # "Two and a Half Men S12"

            if season_name not in data_sections:
                data_sections[season_name] = []


            episode = "{Episode REPLATE}"


            name_episode = k[:len(f"{TVSeriesName} S01E01")][-2:] + ": " + k[len(f"{TVSeriesName} S01E01")+1:]

            # id_episode = 
            dataReplace = f"{name_episode}"
            episode = episode.replace("REPLATE", dataReplace)



            data_subsection = f'\\subsection {episode}'
            # print(idx, season_name, data_subsection)


            scripts = v


            cnt_line = 0

            for idl, line in enumerate(scripts):
                # print(idl, line)
                # exit(0)
                # if idl == 20:
                    # exit(0)
                line = line.replace("♪", "")

                if len(line) > 0:

                    cnt_line += 1
                    data_subsection += "\n" + f'{cnt_line} - {removeRedundantChar(line)}\\\\'
                    # print(data_subsection)
                    # break

            data_subsection = data_subsection[:-2]

            data_sections[season_name].append(data_subsection)

            # print(data_subsection)
        # print(len(data_sections))
        # for idd, (k, vv) in enumerate(data_sections.items()):
        #     print(idd, k, len(vv))
        # return

        # print(data_sections.keys())
        
        # exit(0)


        all_data = ""

        for idd, (k, vv) in enumerate(data_sections.items()):
            

            
            if idd % splitSeason == 0:
                # print("idd", idd, k)         
                all_data = ""

            # print(idx, len(all_data))

            section = "{REPLATE_SECTION}"
            section = section.replace("REPLATE_SECTION", k)
                

            data_section = f"\\section {section}"

            
            for idv, v1 in enumerate(vv):
                data_section += "\n" + v1
            

            if len(all_data) > 0:
                all_data += "\n" + data_section

            else:
                all_data = data_section
            

            if (idd + 1) % splitSeason == 0 or idd == len(data_sections) - 1:
                subtract = idd % splitSeason
                if subtract == 0:
                    subtract = splitSeason
                fileName = f"./{TVShortName}__Season_{idd - subtract + 1:02}_{idd+1:02}.tex"
                # print(fileName)
                # exit(0)

                all_data = TemplateOverleaf.replace("{}", all_data)
                # print(len(all_data))
                # exit(0)

                all_data = all_data.replace("TVSeriesName", TVSeriesName)
                # print("len data: {}".format(len(all_data)))
                open(fileName, "w").write(all_data)
                print("Done write to file: {}".format(fileName))
                # exit(0)


    def genTBBT(self, json_path="./tbbt_scripts.json"): # 279 episode
        data = json.load(open(json_path, "r"))
        
        print(len(data))
        
        data_sections = {}

        # \section{Season 04}\n\

        # \subsection{Episode 03}\n\

        for idx, (k, v) in enumerate(data.items()):
            # if idx == 110:
            #   break

            season_name = f'The Big Bang Theory Season {k[:2]}'
            if season_name not in data_sections:
                data_sections[season_name] = []


            # k = "01x01 - The Pilot"

            # print(idx, k)
            episode = "{Episode REPLATE}"
            name_episode = k.split(" - ")[-1]
            dataReplace = f"{k[3:5]}: {name_episode}"
            episode = episode.replace("REPLATE", dataReplace)
            # episode = "{}"

            data_subsection = f'\\subsection {episode}'

            # print(idx, data_subsection)
            scripts = v["scripts"]

            # print(scripts)
            # print(len(scripts))
            lines = scripts.split("\n")

            cnt_line = 0

            for idl, line in enumerate(lines):
                line = line.replace("♪", "")
                if len(line) > 0:

                    cnt_line += 1
                    data_subsection += "\n" + f'{cnt_line} - {line}\\\\'
                    # print(data_subsection)
                    # break
            data_subsection = data_subsection[:-2]
            data_sections[season_name].append(data_subsection)

        

        for k, v in data_sections.items():

            if k[-2:] == "01" or k[-2:] == "05" or k[-2:] == "09":
                all_data = ""

            section = "{REPLATE_SECTION}"
            section = section.replace("REPLATE_SECTION", k)
            # print(section)
            data_section = f"\\section {section}"
            # print(data_section)
            for v1 in v:
                data_section += "\n" + v1

            # print(data_section)
            if len(all_data) > 0:
                all_data += "\n" + data_section
            else:
                all_data = data_section

            if k[-2:] == "04" or k[-2:] == "08" or k[-2:] == "12":
                if k[-2:] == "04":
                    fileName = "./TheBigBangTheory__Season_01_04.tex"
                elif k[-2:] == "08":
                    fileName = "./TheBigBangTheory__Season_05_08.tex"
                else:
                    fileName = "./TheBigBangTheory__Season_09_12.tex"

                all_data = TemplateOverleaf.replace("{}", all_data)
                all_data = all_data.replace("TVSeriesName", "The Big Bang Theory")
                # open("./TheBigBangTheory12Seasons.tex", "w").write(all_data)
                open(fileName, "w").write(all_data)


genTextOverleaf = GenTextOverleaf()
# print(TemplateOverleaf.replace("{}", "TUAN"))
# print("\\")

# sparkling
# thich uong vang y
