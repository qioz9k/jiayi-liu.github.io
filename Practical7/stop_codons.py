import re

# 打开输入输出文件
infile = open("../Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")
outfile = open("../Practical7/stop_genes.fa", "w")

current_header = ""
current_seq = ""

# 逐行读取（上课教的）
for line in infile:
    line = line.rstrip()

    # 标题行
    if line.startswith(">"):
        # 处理上一个基因
        if current_header and current_seq:
            # 找 ATG
            atg_pos = current_seq.find("ATG")
            if atg_pos != -1:
                # 严格 3 个一组找终止密码子
                found = False
                stop_codon = ""
                for i in range(atg_pos, len(current_seq)-2, 3):
                    c = current_seq[i:i+3]
                    if c in ["TAA", "TAG", "TGA"]:
                        stop_codon = c
                        found = True
                        break
                # 有就写入！
                if found:
                    gene = current_header.split()[0][1:]
                    outfile.write(f">{gene} {stop_codon}\n")
                    outfile.write(current_seq + "\n")

        # 新基因
        current_header = line
        current_seq = ""

    # 序列行
    else:
        current_seq += line

# 最后一个基因
if current_header and current_seq:
    atg_pos = current_seq.find("ATG")
    if atg_pos != -1:
        found = False
        stop_codon = ""
        for i in range(atg_pos, len(current_seq)-2, 3):
            c = current_seq[i:i+3]
            if c in ["TAA", "TAG", "TGA"]:
                stop_codon = c
                found = True
                break
        if found:
            gene = current_header.split()[0][1:]
            outfile.write(f">{gene} {stop_codon}\n")
            outfile.write(current_seq + "\n")

infile.close()
outfile.close()

  