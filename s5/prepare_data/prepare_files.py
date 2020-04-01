# aishell1的transcript文件中的说话人编号BAC009S0002W0122 转换成AISHELL2格式 IS0002W0122
# 因为aishell2采用结巴分词，移除标注的空格

new_transcripts = []
# 注意编码方式，开头有个\ufeff字符
aishell_transcripts = open("./aishell_transcript_v0.8_nospace.txt", "r", encoding="utf-8-sig")

transcripts = aishell_transcripts.readlines()
# 默认编码方式为utf-8
trans_txt = open("./trans.txt", 'w')

for transcript in transcripts:
    spkid = "I" + transcript[6: 16]
    trans = transcript[16: len(transcript)]
    new_transcripts.append(spkid + "\t" + trans)  # 带了\n因此不需要添加换行符

trans_txt.writelines(new_transcripts)
aishell_transcripts.close()
trans_txt.close()


import glob
import os

datadir = "/users/liuli/database/aishellv1/data_aishell/wav/"

for set in ["train", "dev", "test"]:
    new_wav_scp = []
    set_path = os.path.join(datadir, set)
    list_wav = glob.glob(os.path.join(set_path, "*/*.wav"))

    wav_scp = open("wav.scp." + set, "w")

    for filepath in list_wav:
        filename = os.path.basename(filepath)
        spkid = "I" + filename[6: 16]
        relative_path = filepath.replace(set_path + "/", "")
        new_wav_scp.append(spkid + "\t" + relative_path + "\n")

    wav_scp.writelines(new_wav_scp)
    wav_scp.close()

    cp_trans = "cp trans.txt " + set_path
    cp_wav = "cp wav.scp." + set + " " + set_path + "/wav.scp"
    os.system(cp_trans)
    os.system(cp_wav)
