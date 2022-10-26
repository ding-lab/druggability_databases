
# This directory is named 'druggability_databases'

# Read preprocessed DrugBank
drugbank_files = {
    'file':  ''
}

# Read in CIViC
civic_files = {
    'assertions':            'CIViC/01-Oct-2021-AssertionSummaries.tsv',
    'genes':                 'CIViC/01-Oct-2021-GeneSummaries.tsv',
    'variants':              'CIViC/01-Oct-2021-VariantSummaries.lifted.tsv',
    'evidence':              'CIViC/01-Oct-2021-ClinicalEvidenceSummaries.tsv',
    'variantgroups':         'CIViC/01-Oct-2021-VariantGroupSummaries.tsv',
    'variants_preprocessed': 'CIViC/01-Oct-2021-VariantSummaries.preprocessed.tsv',
}
civic_params = {
    'ref_build_liftover': 'GRCh38',
    'upstream_version':   '01-Oct-2021',
}


# Read in current oncokb
oncokb_files = {
    'variants':      'OncoKB/oncokb.annotated.tsv',
    'therapeutics':  'OncoKB/oncokb.therapeutic.tsv',
}
oncokb_params = {
    'date_accessed': '',
}

# Read in gzipped fasta protein file
uniprot_files = {
    'fasta':         'Uniprot/uniprot_sprot.fasta.human.tsv.gz',
}
uniprot_params = {
    'upstream_version': '',
    'date_accessed':    '2022-01-24',
    'md5':              '9d9a5ad72da1e590091a225d654570b1',
}

evidence_level_anno = {
    # CIViC
    'A': 'approved', # renamed from /validated/
    'B': 'clinical',
    'C': 'case study',
    'D': 'preclinical',
    'E': 'inferential',

    # OncoKB
    '1': 'approved', # is: FDA-recognized biomarker predictive of response to an FDA-approved drug in this indication
    '2': 'approved', # is: standard care biomarker recommended by the NCCN or other professional guidelines predictive of response to an FDA-approved drug in this indication
    '3A': 'clinical', # is: compelling clinical evidence supports the biomarker as being predictive of repsonse to a drug in this indication
    '3B': 'clinical', # is: standard care or investigational biomarker predictive of response to an FDA-approved or investigational drug in another indication
    '4': 'preclinical', # is: compelling biological evidence supports the biomarker as being predictive of response to a drug
    'Dx1': 'required for diagnosis', # is: FDA and/or professional guideline-recognized biomarker required for diagnosis in this indication
    'Dx2': 'supports diagnosis', # is: FDA and/or professional guildeline-recognized biomarker that supports diagnosis in this indication
    'Dx3': 'assists diagnosis', # is: biomarker that may assist disease diagnosis in this indication based on clinical evidence
    'R1': 'resistance, standard care', # is: standard care biomarker predictive of resistance to an FDA-approved drug in this indication
    'R2': 'resistance, investigational', # is: compelling clinical evidence supports the biomarker as being predictive of resistance to a drug

    # Miscellaneous
    '-': '-',
}

# Clinical trials
trials_files = {
    'chol':  {'disease_name': 'cholangiocarcinoma', 'summary_file': 'clinical_trials/CHOL.tsv', 'version': '220918'},
    'mm':    {'disease_name': 'multiple myeloma',   'summary_file': 'clinical_trials/MM.tsv',   'version': 'NA'},
    'crc':   {'disease_name': 'colorectal',         'summary_file': 'clinical_trials/CRC.tsv',  'version': 'NA'},
}

# Gene lists
gene_lists = {
    'hgnc_symbols': {'description': 'HGNC gene list',                  'filename': 'HGNC/hgnc_complete_set.txt',      'upstream_version': '2022-03-01',},
    'hr_repair':    {'description': 'homologous recombination repair', 'filename': 'gene_lists/HR_repair_genes.lst', },
    'mm_repair':    {'description': 'mismatch repair',                 'filename': 'gene_lists/MM_repair_genes.lst', },
    'dna_repair':   {'description': 'DNA repair',                      'filename': 'gene_lists/dna_repair_genes.lst',},
}
