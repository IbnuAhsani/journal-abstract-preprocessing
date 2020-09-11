# Text Processing

A collection of text processing methods that's used to create training data for a [Softmax Regression](https://github.com/ssentinull/softmax-regression-module) model.

## Features

- Text preprocessing that includes: digits, whitespaces, and punctuations removal; stop words removal; stemming; tokenization.
- English sentence removal.
- Term Frequency - Inverse Document Frequency (TF-IDF) calculation.
- Journal indexer.
- Long words extractor and replacer.

## How To Run

- Text preprocessing :

    ```shell
    $ python3 preprocess_abstract.py
    ```

- English sentence removal :

    ```shell
    $ python3 remove_english_sentence.py
    ```

- Journal indexer :
    
    ```shell
    $ python3 preprocess_abstract.py
    ```

- Long words extractor :

    ```shell
    $ python3 extract_long_words.py
    ```

- Long words replacer :

    ```shell
    $ python3 replace_long_words.py
    ```

## Input

Text preprocessing, english sentence removal, journal indexer, as well as long words extractor and replacer uses the same file as input. That file can be found in `./data/input/dataset-sample.csv` directory and it looks like this :

```csv
JOURNAL_TITLE,ARTICLE_TITLE,ARTICLE_ABSTRACT
Buletin Ekonomi Moneter dan Perbankan,KRISIS KEUANGAN GLOBAL DAN PERTUMBUHAN EKONOMI: ANALISA DARI PEREKONOMIAN ASIA TIMUR ,"Sejalan dengan semakin terintegrasinya perekonomian di ... Ekonomi Asia Timur, Pertumbuhan Ekonomi, Pasar Finansial, Efek Acak dan TetapJEL Classification: C330, E440, G010"
Buletin Ekonomi Moneter dan Perbankan,ANALISIS TRIWULAN III - 2012 ,"Perekonomian domestik masih tumbuh cukup baik walaupun mengalami sedikit perlambatan ... Indonesia untuk keseluruhan tahun 2012 diprakirakan tumbuh 6,3% dan pada tahun 2013 meningkat menuju kisaran 6,3%-6,7%."
```

## Output

- Text preprocessing : `./data/output/preprocessed-dataset-sample.json`

    ```
    [
        {
            "JOURNAL_ID": 20,
            "JOURNAL_TITLE": "Jurnal Rekayasa Sistem & Industri (JRSI)",
            "ARTICLE_ID": 10465,
            "ARTICLE_TITLE": "PERANCANGAN MODEL OPTIMASI ALOKASI JUMLAH SERVER UNTUK MEMINIMALKAN TOTAL ANTREAN PADA SISTEM ANTREAN DUA ARAH PADA GERBANG TOL ",
            "ARTICLE_ABSTRACT": "Terdapat beberapa sistem antrean menggunakan sistem dua arah input dan output pada ... pelayanan memoryless dengan distribusi binomial, dan jumlah server lebih dari satu.  Panjang antrean tidak dibatasi, jumlah populasi tidak dibatasi",
            "TOKENS": ["sistem", "antre", "sistem", "arah", "input", "output", ... , "memoryless", "distribusi", "binomial", "server", "antre", "batas", "populasi", "batas"],
            "TOKENS_DUPLICATE_REMOVED": ["sistem", "antre", "arah", "input", "output", "gerbang", ... , "memoryless", "distribusi", "poisson", "layan", "binomial", "server", "batas", "populasi" ]
        },
        ... ,
        {
            "JOURNAL_ID": integer,
            "JOURNAL_TITLE": string,
            "ARTICLE_ID": integer,
            "ARTICLE_TITLE": string,
            "ARTICLE_ABSTRACT": string,
            "TOKENS": list,
            "TOKENS_DUPLICATE_REMOVED": list
        }
    ]
    ```

- English sentence removal : `./data/output/data-sample-english-sentence-removed.csv`

    ```csv
    JOURNAL_TITLE,ARTICLE_TITLE,ARTICLE_ABSTRACT
    Buletin Ekonomi Moneter dan Perbankan,KRISIS KEUANGAN GLOBAL DAN PERTUMBUHAN EKONOMI: ANALISA DARI PEREKONOMIAN ASIA TIMUR ,"Sejalan dengan semakin terintegrasinya perekonomian di ... Ekonomi Asia Timur, Pertumbuhan Ekonomi, Pasar Finansial, Efek Acak dan TetapJEL Classification: C330, E440, G010"
    Buletin Ekonomi Moneter dan Perbankan,ANALISIS TRIWULAN III - 2012 ,"Perekonomian domestik masih tumbuh cukup baik walaupun mengalami sedikit perlambatan ... Indonesia untuk keseluruhan tahun 2012 diprakirakan tumbuh 6,3% dan pada tahun 2013 meningkat menuju kisaran 6,3%-6,7%."
    ```

- Journal indexer : `./data/output/data-sample-indexed.csv`
    
    ```
    JOURNAL_ID,JOURNAL_TITLE,ARTICLE_ID,ARTICLE_TITLE,ARTICLE_ABSTRACT
    0,Jurnal Pendidikan IPA Indonesia,0,PEMETAAN KETERAMPILAN ESENSIAL LABORATORIUM DALAM KEGIATAN PRAKTIKUM EKOLOGI ,"Keterampilan esensial laboratorium adalah keterampilan ... students laboratory essential skill achievement level is 35,50%. This research is aimed to analyze the competency profile of essential laboratory skill for biology teacher candidate."
    0,Jurnal Pendidikan IPA Indonesia,1,PENGEMBANGAN MODUL MATA KULIAH STRATEGI BELAJAR MENGAJAR IPA  BERBASIS HASIL PENELITIAN PEMBELAJARAN ,"Tujuan penelitian ini adalah untuk mengembangkan bahan ajar melalui pemanfaatan ... results are feasible to use as reference to develop the modul because it is considered to be more applicative and fulfill the novelty aspect."
    1,Buletin Ekonomi Moneter dan Perbankan,3,KRISIS KEUANGAN GLOBAL DAN PERTUMBUHAN EKONOMI: ANALISA DARI PEREKONOMIAN ASIA TIMUR ,"Sejalan dengan semakin terintegrasinya perekonomian di tengah eraglobalisasi, krisis keuangan yang terjadi pada suatu negara dapat dengan ... krisis global pada tahun 2008.Kata kunci: Krisis Keuangan Global; Ekonomi Asia Timur, Pertumbuhan Ekonomi, Pasar Finansial, Efek Acak dan TetapJEL Classification: C330, E440, G010"
    ```

- Long words extractor : `./data/output/joined-words.json` 

    ```
    {
        "eraglobalisasi,": "eraglobalisasi,",
        "pasarmemburuk.": "pasarmemburuk.",
        "tersebutberasal": "tersebutberasal",
         ... ,
        "meningkat.Konsumsi": "meningkat.Konsumsi",
        "mendorongmeningkatnya": "mendorongmeningkatnya",
        "perlambatanperekonomian": "perlambatanperekonomian"
    }
    ```

- Long words replacer : `./data/output/data-sample-joined-words-removed.csv`

    ```csv
    JOURNAL_TITLE,ARTICLE_TITLE,ARTICLE_ABSTRACT
    Buletin Ekonomi Moneter dan Perbankan,KRISIS KEUANGAN GLOBAL DAN PERTUMBUHAN EKONOMI: ANALISA DARI PEREKONOMIAN ASIA TIMUR ,"Sejalan dengan semakin terintegrasinya perekonomian di ... Ekonomi Asia Timur, Pertumbuhan Ekonomi, Pasar Finansial, Efek Acak dan TetapJEL Classification: C330, E440, G010"
    Buletin Ekonomi Moneter dan Perbankan,ANALISIS TRIWULAN III - 2012 ,"Perekonomian domestik masih tumbuh cukup baik walaupun mengalami sedikit perlambatan ... Indonesia untuk keseluruhan tahun 2012 diprakirakan tumbuh 6,3% dan pada tahun 2013 meningkat menuju kisaran 6,3%-6,7%."
    ```

## Library Used

- [nltk](https://pypi.org/project/nltk/)
- [Sastrawi](https://pypi.org/project/Sastrawi/)

## License

MIT © [ssentinull](https://github.com/ssentinull)