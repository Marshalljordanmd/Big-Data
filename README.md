# Big-Data
Python scripts to analyze whole chromosome files of the 1000 Genome Project. These vcf files were from International Genome Project  (www.internationalgenome.org)

"big_data.py"  gets the AF from the INFO line of the vcf chromosome files, categorizing them as Rare (<0.5%), Uncommon (0.5-5%), and Common (>5%)

The other python scripts obtain the allele frequency of each variant row in the vcf files by counting genotypes from the 2504 sample columns and computing the AF from AC/AN.

"genotype.py" counts the individual sample genotypes to get AC and divides by 2504 to get AF. the AF are grouped into Rare, Uncommon, and Common according the above frequency categories.

"new_x.py" counts the genotypes to compute AF for the chrX, using 2504 for the PAR regions, and 3775 for the main part of X.

"male_var.py" and "male_var_x.py" count genotypes to get the AF for the autosomes and chrX respectively.

"female_var.py" counts the female genotypes to get the AF for females on the autosomes and the X.

"y_segs.py" counts the genotypes to get AF on segments of the chrY which comprise the 10.4 MB mask used for the Y in the 1000 Genome Project.
