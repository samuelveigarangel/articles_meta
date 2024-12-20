# coding: utf-8
import unittest
import json
import os
import io

from lxml import etree as ET

from articlemeta import export_crossref
from articlemeta import export
from articlemeta.export import CustomArticle as Article


def _get_article(data=None):
    article_json = {
        "fulltexts": {
            "pdf": {
                "es": "http://www.scielo.br/pdf/rsp/v44n4/es_07.pdf",
                "en": "http://www.scielo.br/pdf/rsp/v44n4/en_07.pdf",
                "pt": "http://www.scielo.br/pdf/rsp/v44n4/07.pdf"
            },
            "html": {
                "es": "http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0034-89102010000400007&tlng=es",
                "en": "http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0034-89102010000400007&tlng=en",
                "pt": "http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0034-89102010000400007&tlng=pt"
            }
        },
        "collection": "scl",
        "doi": "10.1590/S0034-89102010000400007",
        "body": {
            "pt": "Body PT",
            "es": "Body ES",
            "en": "Body EN"
        },
        "article": {
            "v880": [
                {
                    "_": "S0034-89102010000400007"
                }
            ],
            "v237": [
                {
                    "_": "10.1590/S0034-89102010000400007"
                }
            ],


            "v40": [
                {
                    "_": "pt"
                }
            ],

            "v12": [
                {
                    "l": "pt",
                    "_": "Perfil epidemiológico dos pacientes em terapia"
                    " renal substitutiva no Brasil, 2000-2004"
                },
                {
                    "l": "en",
                    "_": "Epidemiological profile of patients on"
                    " renal replacement therapy in Brazil, 2000-2004"
                },
                {
                    "l": "es",
                    "_": "Perfil epidemiológico de los pacientes en terapia"
                    " renal substitutiva en Brasil, 2000-2004"
                }
            ],
            "v337": [
                {
                    "l": "pt",
                    "d": "10.1590/S0034-89102010000400007",
                },
                {
                    "l": "es",
                    "d": "10.1590/ID.es"
                }

            ],
            "v83": [
                {
                    "a": "OBJETIVO: Descrever o perfil epidemiol\u00f3gico e cl\u00ednico de pacientes em terapia renal substitutiva, identificando fatores associados ao risco de morte. M\u00c9TODOS: Estudo observacional, prospectivo n\u00e3o concorrente, a partir de dados de 90.356 pacientes da Base Nacional em Terapias Renais Substitutivas, no Brasil. Foi realizado relacionamento determin\u00edstico-probabil\u00edstico do Sistema de Autoriza\u00e7\u00e3o de Procedimentos de Alta Complexidade/Custo e do Sistema de Informa\u00e7\u00e3o de Mortalidade. Foram inclu\u00eddos todos os pacientes incidentes que iniciaram di\u00e1lise entre 1/1/2000 e 31/12/2004, acompanhados at\u00e9 a morte ou final de 2004. Idade, sexo, regi\u00e3o de resid\u00eancia, doen\u00e7a renal prim\u00e1ria, causa do \u00f3bito foram analisados. Ajustou-se um modelo de riscos proporcionais para identificar fatores associados ao risco de morte. RESULTADOS: Ocorreu um aumento m\u00e9dio de 5,5% na preval\u00eancia de pacientes em terapia enquanto a incid\u00eancia manteve-se est\u00e1vel no per\u00edodo. Hemodi\u00e1lise foi a modalidade inicial predominante (89%). A maioria dos pacientes era do sexo masculino, com idade m\u00e9dia de 53 anos, residente na regi\u00e3o Sudeste, e apresentava causa indeterminada como principal causa b\u00e1sica da doen\u00e7a renal cr\u00f4nica, seguida da hipertens\u00e3o, diabetes e glomerulonefrites. Desses pacientes, 7% realizou transplante renal e 42% evoluiu para o \u00f3bito. Os pacientes em di\u00e1lise peritoneal eram mais idosos e apresentavam maior preval\u00eancia de diabetes. Entre os n\u00e3o transplantados, 45% foi a \u00f3bito e, entre os transplantados, 7%. No modelo final de riscos proporcionais de Cox, o risco de mortalidade foi associado com o aumento da idade, sexo feminino, ter diabetes, residir nas regi\u00f5es Norte e Nordeste, di\u00e1lise peritoneal como modalidade de entrada e n\u00e3o ter realizado transplante renal. CONCLUS\u00d5ES: Houve aumento da preval\u00eancia de pacientes em terapia renal no Brasil. Pacientes com idade avan\u00e7ada, diabetes, do sexo feminino, residentes nas regi\u00f5es Norte e Nordeste e sem transplante renal apresentam maior risco de morte.",
                    "l": "pt",
                    "_": ""
                },
                {
                    "a": "OBJECTIVE: To describe the clinical and epidemiological profile of patients under renal replacement therapies, identifying risk factors for death. METHODS: This is a non-concurrent cohort study of data for 90,356 patients in the National Renal Replacement Therapies Database. A deterministic-probabilistic linkage was performed using the Authorization System for High Complexity/Cost Procedures and the Mortality Information System databases. All patients who started dialysis between 1/1/2000 and 12/31/2004 were included and followed until death or the end of 2004. Age, sex, region of residence, primary renal disease and causes of death were analyzed. A proportional hazards model was used to identify factors associated with risk of death. RESULTS: The prevalence of patients under renal replacement therapies increased an average of 5.5%, while incidence remained stable during the period. Hemodialysis was the predominant initial modality (89%). The patients were majority male with mean age 53 years, residents of the Southeast region and presented unknown causes as the main cause of chronic renal disease, followed by hypertension, diabetes and glomerulonephritis. Of these patients, 42% progressed to death and 7% underwent kidney transplantation. The patients on peritoneal dialysis were older and had higher prevalence of diabetes. The death rate varied from 7% among transplanted patients to 45% among non-transplanted patients. In the final Cox proportional hazards model, the risk of mortality was associated with increasing age, female sex, having diabetes, living in the North and Northeast region, peritoneal dialysis as a first modality and not having renal transplantation. CONCLUSIONS: There was an increased prevalence of patients on renal therapy in Brazil. Increased risk of death was associated with advanced age, diabetes, the female sex, residents of the North and Northeast region and lack of renal transplant.",
                    "l": "en",
                    "_": ""
                },
                {
                    "a": "OBJETIVO: Describir el perfil epidemiol\u00f3gico y cl\u00ednico de pacientes en terapia renal substitutiva, identificando factores asociados al riesgo de muerte. M\u00c9TODOS: Estudio de observaci\u00f3n, prospectivo no concurrente, a partir de datos de 90.356 pacientes de la Base Nacional en Terapias Renales Substitutivas, en Brasil. Fue realizado reracionamiento determin\u00edstico-probabil\u00edstico del Sistema de Informaci\u00f3n de Mortalidad. Fueron incluidos todos los pacientes incidentes que iniciaron di\u00e1lisis entre 1/1/2000 y 31/12/2004, acompa\u00f1ados hasta la muerte o final de 2004. Edad, sexo, regi\u00f3n de residencia, enfermedad renal primaria, causa del \u00f3bito fueron analizados. Se ajust\u00f3 un modelo de riesgos proporcionales para identificar factores asociados al riesgo de muerte. RESULTADOS: Ocurri\u00f3 un aumento promedio de 5,5% en la prevalencia de pacientes en terapia, con relaci\u00f3n a la incidencia se mantuvo estable en el per\u00edodo. Hemodi\u00e1lisis fue la modalidad inicial predominante (89%). La mayor\u00eda de los pacientes era del sexo masculino, con edad promedio de 53 a\u00f1os, residente en la regi\u00f3n Sureste y presentaba causa indeterminada como principal causa b\u00e1sica de la enfermedad renal cr\u00f3nica, seguida de la hipertensi\u00f3n, diabetes y glomerulonefritis. De esos pacientes, 7% realizaron transplante renal y 42% evolucionaron a \u00f3bito. Los pacientes en di\u00e1lisis peritoneal eran m\u00e1s ancianos y presentaban mayor prevalencia de diabetes. Entre los no transplantados, 45% fueron a \u00f3bito y, entre los transplantadas 7%. En el modelo final de riesgos proporcionales de Cox, el riesgo de mortalidad estuvo asociado con el aumento de la edad, sexo femenino, tener diabetes, residir en la regi\u00f3n Norte y Noreste, di\u00e1lisis peritoneal como modalidad de entrada y no haber realizado transplante renal. CONCLUSIONES: Hubo aumento de la prevalencia de pacientes en terapia renal en Brasil. Pacientes con edad avanzada, diabetes, del sexo femenino, residentes en la regi\u00f3n Norte y Noreste y sin transplante renal presentan mayor riesgo de muerte.",
                    "l": "es",
                    "_": ""
                }
            ]
        },

        "issue": {
            "issue": {},
        },
    }
    data = data or {}
    article_json["article"].update(data)
    return Article(article_json)


def create_xmlcrossref_with_journal_element(journal_child_name=None):
    xmlcrossref = ET.Element('doi_batch')
    journal = ET.Element('journal')
    if journal_child_name:
        journal_child = ET.Element(journal_child_name)
        journal.append(journal_child)
    body = ET.Element('body')
    body.append(journal)

    xmlcrossref.append(body)
    return xmlcrossref


def create_xmlcrossref_with_n_journal_article_element(
        languages, journal_article_child_name=None):

    journal_article_child = (
        journal_article_child_name and f"<{journal_article_child_name}/>" or ''
    )
    items = []
    for lang in languages:
        items.append(
            f'<journal_article language="{lang}" publication_type="full_text">'
            f'{journal_article_child}'
            '</journal_article>'
        )
    journal_articles = "\n".join(items)
    xml = (
        '<doi_batch>'
        '<body>'
        '<journal>'
        f'{journal_articles}'
        '</journal>'
        '</body>'
        '</doi_batch>'
    )
    return ET.fromstring(xml)


class ExportCrossRefTitleDoiLangTests(unittest.TestCase):

    def setUp(self):
        self._article = _get_article()

    def test_title_doi_lang_for_article_which_has_one_doi_and_one_title(self):
        data = {"v337": [], "v12": []}
        data["v12"] = [
            {
                "l": "pt",
                "_": (
                    "Perfil epidemiológico dos pacientes em terapia"
                    " renal substitutiva no Brasil, 2000-2004"
                )
            }
        ]
        article = _get_article(data)
        expected = {
            "pt": {
                "article_title": (
                    "Perfil epidemiológico dos pacientes em terapia"
                    " renal substitutiva no Brasil, 2000-2004"
                ),
                "doi": "10.1590/S0034-89102010000400007",
                "original": True,
            }
        }
        result = export_crossref.title_doi_lang(article)
        self.assertEqual(expected, result)

    def test_title_doi_lang_for_article_which_has_one_doi_and_titles(self):
        data = {"v337": []}
        article = _get_article(data)
        expected = {
            "pt": {
                "article_title": (
                    "Perfil epidemiológico dos pacientes em terapia"
                    " renal substitutiva no Brasil, 2000-2004"
                ),
                "doi": "10.1590/S0034-89102010000400007",
                "original": True,
            },
            "en": {
                "article_title": (
                    "Epidemiological profile of patients on"
                    " renal replacement therapy in Brazil, 2000-2004"
                )
            },
            "es": {
                "article_title": (
                    "Perfil epidemiológico de los pacientes en terapia"
                    " renal substitutiva en Brasil, 2000-2004"
                )
            }
        }
        result = export_crossref.title_doi_lang(article)
        self.assertEqual(expected, result)

    def test_title_doi_lang_for_article_which_has_multiple_dois_and_titles(self):
        article = _get_article()
        expected = {
            "pt": {
                "article_title": (
                    "Perfil epidemiológico dos pacientes em terapia"
                    " renal substitutiva no Brasil, 2000-2004"
                ),
                "doi": "10.1590/S0034-89102010000400007",
                "original": True,
            },
            "en": {
                "article_title": (
                    "Epidemiological profile of patients on"
                    " renal replacement therapy in Brazil, 2000-2004"
                )
            },
            "es": {
                "article_title": (
                    "Perfil epidemiológico de los pacientes en terapia"
                    " renal substitutiva en Brasil, 2000-2004"
                ),
                "doi": "10.1590/ID.es",
            }
        }
        result = export_crossref.title_doi_lang(article)
        self.assertEqual(expected, result)


class ExportCrossRef_one_DOI_only_Tests(unittest.TestCase):

    def setUp(self):
        with open(
                os.path.dirname(__file__)+'/fixtures/article_meta.json') as fp:
            self._raw_json = json.loads(fp.read())
        self._article_meta = Article(self._raw_json)

    def test_doi_batch_element(self):

        data = [None, None]

        xmlcrossref = export_crossref.SetupDoiBatchPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual('doi_batch', xml.tag)

    def test_doi_batch_id_element(self):

        xmlcrossref = ET.Element('doi_batch')

        xmlcrossref.append(ET.Element('head'))

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLDoiBatchIDPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual('doi_batch_id', xml.find('head/doi_batch_id').tag)

    def test_depositor_element(self):

        xmlcrossref = ET.Element('doi_batch')

        xmlcrossref.append(ET.Element('head'))

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLDepositorPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(b'<doi_batch><head><depositor><depositor_name>depositor</depositor_name><email_address>name@domain.com</email_address></depositor></head></doi_batch>', ET.tostring(xml))

    def test_registrant_element(self):

        xmlcrossref = ET.Element('doi_batch')

        xmlcrossref.append(ET.Element('head'))

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLRegistrantPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(b'<doi_batch><head><registrant>registrant</registrant></head></doi_batch>', ET.tostring(xml))

    def test_time_stamp_element(self):

        xmlcrossref = ET.Element('doi_batch')

        xmlcrossref.append(ET.Element('head'))

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLTimeStampPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual('timestamp', xml.find('head/timestamp').tag)

    def test_head_element(self):

        xmlcrossref = ET.Element('doi_batch')

        data = [None, xmlcrossref]

        xmlcrossref = export_crossref.XMLHeadPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual('head', xml.find('head').tag)

    def test_body_element(self):

        xmlcrossref = ET.Element('doi_batch')

        data = [None, xmlcrossref]

        xmlcrossref = export_crossref.XMLBodyPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual('body', xml.find('body').tag)

    def test_journal_element(self):

        xmlcrossref = ET.Element('doi_batch')

        xmlcrossref.append(ET.Element('body'))

        data = [None, xmlcrossref]

        xmlcrossref = export_crossref.XMLJournalPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(b'<doi_batch><body><journal/></body></doi_batch>', ET.tostring(xml))

    def test_journal_metadata_element(self):

        xmlcrossref = ET.Element('doi_batch')

        body = ET.Element('body')
        body.append(ET.Element('journal'))

        xmlcrossref.append(body)

        data = [None, xmlcrossref]

        xmlcrossref = export_crossref.XMLJournalMetadataPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(b'<doi_batch><body><journal><journal_metadata/></journal></body></doi_batch>', ET.tostring(xml))

    def test_journal_title_element(self):

        xmlcrossref = ET.Element('doi_batch')

        journal = ET.Element('journal')
        journal.append(ET.Element('journal_metadata'))

        body = ET.Element('body')
        body.append(journal)

        xmlcrossref.append(body)

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLJournalTitlePipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(b'<doi_batch><body><journal><journal_metadata><full_title>Revista de Sa&#250;de P&#250;blica</full_title></journal_metadata></journal></body></doi_batch>', ET.tostring(xml))

    def test_abbreviated_journal_title_element(self):

        xmlcrossref = ET.Element('doi_batch')

        journal = ET.Element('journal')
        journal.append(ET.Element('journal_metadata'))

        body = ET.Element('body')
        body.append(journal)

        xmlcrossref.append(body)

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLAbbreviatedJournalTitlePipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(b'<doi_batch><body><journal><journal_metadata><abbrev_title>Rev. Sa&#250;de P&#250;blica</abbrev_title></journal_metadata></journal></body></doi_batch>', ET.tostring(xml))

    def test_journal_issn_element(self):

        xmlcrossref = ET.Element('doi_batch')

        journal = ET.Element('journal')
        journal.append(ET.Element('journal_metadata'))

        body = ET.Element('body')
        body.append(journal)

        xmlcrossref.append(body)

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLISSNPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(b'<doi_batch><body><journal><journal_metadata><issn media_type="print">0034-8910</issn></journal_metadata></journal></body></doi_batch>', ET.tostring(xml))

    def test_journal_issue_element(self):

        xmlcrossref = ET.Element('doi_batch')

        body = ET.Element('body')
        body.append(ET.Element('journal'))

        xmlcrossref.append(body)

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLJournalIssuePipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(b'<doi_batch><body><journal><journal_issue/></journal></body></doi_batch>', ET.tostring(xml))

    def test_publication_date_element(self):

        xmlcrossref = ET.Element('doi_batch')

        journal = ET.Element('journal')
        journal.append(ET.Element('journal_issue'))

        body = ET.Element('body')
        body.append(journal)

        xmlcrossref.append(body)

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLPubDatePipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(b'<doi_batch><body><journal><journal_issue><publication_date media_type="online"><month>08</month><year>2010</year></publication_date></journal_issue></journal></body></doi_batch>', ET.tostring(xml))

    def test_volume_element(self):

        xmlcrossref = ET.Element('doi_batch')

        journal = ET.Element('journal')
        journal.append(ET.Element('journal_issue'))

        body = ET.Element('body')
        body.append(journal)

        xmlcrossref.append(body)

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLVolumePipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(b'<doi_batch><body><journal><journal_issue><journal_volume><volume>44</volume></journal_volume></journal_issue></journal></body></doi_batch>', ET.tostring(xml))

    def test_number_element(self):

        xmlcrossref = ET.Element('doi_batch')

        journal = ET.Element('journal')
        journal.append(ET.Element('journal_issue'))

        body = ET.Element('body')
        body.append(journal)

        xmlcrossref.append(body)

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLIssuePipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(b'<doi_batch><body><journal><journal_issue><issue>4</issue></journal_issue></journal></body></doi_batch>', ET.tostring(xml))

    def test_journal_article_element(self):

        xmlcrossref = ET.Element('doi_batch')

        body = ET.Element('body')
        body.append(ET.Element('journal'))

        xmlcrossref.append(body)

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLJournalArticlePipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(b'<doi_batch><body><journal><journal_article language="pt" publication_type="full_text" reference_distribution_opts="any"/></journal></body></doi_batch>', ET.tostring(xml))

    def test_article_titles_element(self):

        xmlcrossref = ET.Element('doi_batch')

        journal_article = ET.Element('journal_article')
        journal_article.set('publication_type', 'full_text')

        journal = ET.Element('journal')
        journal.append(journal_article)

        body = ET.Element('body')
        body.append(journal)

        xmlcrossref.append(body)

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLArticleTitlesPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(b'<doi_batch><body><journal><journal_article publication_type="full_text"><titles/></journal_article></journal></body></doi_batch>', ET.tostring(xml))

    def test_article_title_element(self):

        xml = (
            '<doi_batch>'
            '<body>'
            '<journal>'
            '<journal_article language="pt" publication_type="full_text">'
            '<titles/>'
            '</journal_article>'
            '<journal_article language="en" publication_type="full_text">'
            '<titles/>'
            '</journal_article>'
            '<journal_article language="es" publication_type="full_text">'
            '<titles/>'
            '</journal_article>'
            '</journal>'
            '</body>'
            '</doi_batch>'
        )
        xmlcrossref = ET.fromstring(xml)

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLArticleTitlePipe()
        raw, xml = xmlcrossref.transform(data)

        expected_titles = [
            'Perfil epidemiológico dos pacientes em terapia renal substitutiva no Brasil, 2000-2004',
            'Epidemiological profile of patients on renal replacement therapy in Brazil, 2000-2004',
            'Perfil epidemiológico de los pacientes en terapia renal substitutiva en Brasil, 2000-2004',
        ]
        expected_alt_titles = [
            'Epidemiological profile of patients on renal replacement therapy in Brazil, 2000-2004',
            'Perfil epidemiológico dos pacientes em terapia renal substitutiva no Brasil, 2000-2004',
            'Epidemiological profile of patients on renal replacement therapy in Brazil, 2000-2004',
        ]
        
        titles = [node.text for node in xml.findall(".//journal_article//title")]
        alt_titles = [node.text for node in xml.findall(".//journal_article//original_language_title")]

        self.assertEqual(expected_titles, titles)
        self.assertEqual(expected_alt_titles, alt_titles)

    def test_article_contributors_element(self):

        raw_json = self._raw_json.copy()

        raw_json['article']['v10'][0]['r'] = 'ed'
        raw_json['article']['v10'][1]['r'] = 'org'
        raw_json['article']['v10'][2]['r'] = 'tr'
        raw_json['article']['v10'][3]['r'] = 'coord'
        raw_json['article']['v10'][-1]['r'] = 'inventor'

        self._article_meta = Article(raw_json)

        xmlcrossref = ET.Element('doi_batch')

        journal_article = ET.Element('journal_article')
        journal_article.set('publication_type', 'full_text')

        journal = ET.Element('journal')
        journal.append(journal_article)

        body = ET.Element('body')
        body.append(journal)

        xmlcrossref.append(body)

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLArticleContributorsPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(b'<doi_batch><body><journal><journal_article publication_type="full_text"><contributors><person_name contributor_role="editor" sequence="first"><given_name>Mariangela Leal</given_name><surname>Cherchiglia</surname><affiliation>Universidade Federal de Minas Gerais,  BRAZIL</affiliation></person_name><person_name contributor_role="author" sequence="additional"><given_name>Elaine Leandro</given_name><surname>Machado</surname><affiliation>Universidade Federal de Minas Gerais,  BRAZIL</affiliation></person_name><person_name contributor_role="translator" sequence="additional"><given_name>Daniele Ara&#250;jo Campo</given_name><surname>Szuster</surname><affiliation>Universidade Federal de Minas Gerais,  BRAZIL</affiliation></person_name><person_name contributor_role="author" sequence="additional"><given_name>Eli Iola Gurgel</given_name><surname>Andrade</surname><affiliation>Universidade Federal de Minas Gerais,  BRAZIL</affiliation></person_name><person_name contributor_role="author" sequence="additional"><given_name>Francisco de Assis</given_name><surname>Ac&#250;rcio</surname><affiliation>Universidade Federal de Minas Gerais,  BRAZIL</affiliation></person_name><person_name contributor_role="author" sequence="additional"><given_name>Waleska Teixeira</given_name><surname>Caiaffa</surname><affiliation>Universidade Federal de Minas Gerais,  BRAZIL</affiliation></person_name><person_name contributor_role="author" sequence="additional"><given_name>Ricardo</given_name><surname>Sesso</surname><affiliation>Universidade Federal de S&#227;o Paulo,  BRAZIL</affiliation></person_name><person_name contributor_role="author" sequence="additional"><given_name>Augusto A</given_name><surname>Guerra Junior</surname><affiliation>Universidade Federal de Minas Gerais,  BRAZIL; Universidade Federal de S&#227;o Paulo,  BRAZIL</affiliation></person_name><person_name contributor_role="author" sequence="additional"><given_name>Odilon Vanni de</given_name><surname>Queiroz</surname><affiliation>Universidade Federal de Minas Gerais,  BRAZIL</affiliation></person_name><person_name contributor_role="author" sequence="additional"><given_name>Isabel Cristina</given_name><surname>Gomes</surname><affiliation>Universidade Federal de Minas Gerais,  BRAZIL</affiliation></person_name></contributors></journal_article></journal></body></doi_batch>', ET.tostring(xml))

    def test_article_publication_date_element(self):

        xmlcrossref = ET.Element('doi_batch')

        journal_article = ET.Element('journal_article')
        journal_article.set('publication_type', 'full_text')

        journal = ET.Element('journal')
        journal.append(journal_article)

        body = ET.Element('body')
        body.append(journal)

        xmlcrossref.append(body)

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLArticlePubDatePipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(b'<doi_batch><body><journal><journal_article publication_type="full_text"><publication_date media_type="online"><month>08</month><year>2010</year></publication_date></journal_article></journal></body></doi_batch>', ET.tostring(xml))

    def test_article_pages_element(self):
        self._article_meta.data['article']['v14'].pop()
        xmlcrossref = ET.Element('doi_batch')

        journal_article = ET.Element('journal_article')
        journal_article.set('publication_type', 'full_text')

        journal = ET.Element('journal')
        journal.append(journal_article)

        body = ET.Element('body')
        body.append(journal)

        xmlcrossref.append(body)

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLPagesPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(b'<doi_batch><body><journal><journal_article publication_type="full_text"><pages><first_page>639</first_page><last_page>649</last_page></pages></journal_article></journal></body></doi_batch>', ET.tostring(xml))

    def test_article_pid_element(self):

        xmlcrossref = ET.Element('doi_batch')

        journal_article = ET.Element('journal_article')
        journal_article.set('publication_type', 'full_text')

        journal = ET.Element('journal')
        journal.append(journal_article)

        body = ET.Element('body')
        body.append(journal)

        xmlcrossref.append(body)

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLPIDPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(b'<doi_batch><body><journal><journal_article publication_type="full_text"><publisher_item><identifier id_type="pii">S0034-89102010000400007</identifier></publisher_item></journal_article></journal></body></doi_batch>', ET.tostring(xml))

    def test_xmlclose_pipe(self):

        pxml = ET.Element('doi_batch')
        pxml.append(ET.Element('head'))

        data = [None, pxml]

        xmlarticle = export_crossref.XMLClosePipe()
        xml = xmlarticle.transform(data)

        self.assertEqual("<?xml version='1.0' encoding='utf-8'?>\n<doi_batch><head/></doi_batch>".encode('utf-8'), xml)

    def test_validating_against_schema(self):

        xml = export.Export(self._raw_json).pipeline_crossref()

        xmlio = ET.parse(io.BytesIO(xml))

        fp = open(os.path.dirname(__file__)+'/xsd/scielo_crossref/crossref4.4.0.xsd')
        schema_root = ET.parse(fp)
        schema = ET.XMLSchema(schema_root)
        fp.close()

        schema.assertValid(xmlio)
        self.assertTrue(schema.validate(xmlio))
        self.assertEqual(None, schema.assertValid(xmlio))

    def test_journal_article_should_contain_item_number_with_elocation_id(self):
        xmlcrossref = ET.Element("doi_batch")
        publisher_item = ET.Element("publisher_item")
        journal_article = ET.Element("journal_article")
        journal_article.set("publication_type", "full_text")
        journal_article.append(publisher_item)

        journal = ET.Element("journal")
        journal.append(journal_article)

        body = ET.Element("body")
        body.append(journal)

        xmlcrossref.append(body)

        data = [self._article_meta, xmlcrossref]
        xmlcrossref = export_crossref.XMLElocationPipe()
        _, xml = xmlcrossref.transform(data)

        self.assertEqual(
            b'<doi_batch><body><journal><journal_article publication_type="full_text"><publisher_item><item_number item_number_type="article_number">53</item_number></publisher_item></journal_article></journal></body></doi_batch>',
            ET.tostring(xml)
        )

    def test_elocation_id_pipeline_should_create_publisher_item(self):
        self._article_meta.data['article']['v14'].pop(0)
        xmlcrossref = ET.Element("doi_batch")
        journal_article = ET.Element("journal_article")
        journal_article.set("publication_type", "full_text")
        journal = ET.Element("journal")
        journal.append(journal_article)

        body = ET.Element("body")
        body.append(journal)

        xmlcrossref.append(body)

        data = [self._article_meta, xmlcrossref]
        xmlcrossref = export_crossref.XMLElocationPipe()
        _, xml = xmlcrossref.transform(data)

        self.assertEqual(
            b'<doi_batch><body><journal><journal_article publication_type="full_text"><publisher_item><item_number item_number_type="article_number">53</item_number></publisher_item></journal_article></journal></body></doi_batch>',
            ET.tostring(xml)
        )

    def test_journal_article_should_not_contains_publisher_item_and_item_number(self):
        self._article_meta.data['article']['v14'].pop()
        xmlcrossref = ET.Element("doi_batch")

        journal_article = ET.Element("journal_article")
        journal_article.set("publication_type", "full_text")

        journal = ET.Element("journal")
        journal.append(journal_article)

        body = ET.Element("body")
        body.append(journal)

        xmlcrossref.append(body)

        data = [self._article_meta, xmlcrossref]

        xmlcrossref = export_crossref.XMLElocationPipe()
        _, xml = xmlcrossref.transform(data)

        self.assertEqual(
            b'<doi_batch><body><journal><journal_article publication_type="full_text"/></journal></body></doi_batch>',
            ET.tostring(xml),
        )


    def test_every_journal_article_must_contain_own_license(self):
            self._article_meta.data["license"] = "by/4.0"

            xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
                ["pt", "en", "es"]
            )

            data = [self._article_meta, xmlcrossref]
            xmlcrossref = export_crossref.XMLPermissionsPipe()
            _, xml = xmlcrossref.transform(data)

            programs = xml.findall(
                ".//{http://www.crossref.org/AccessIndicators.xsd}program"
            )
            self.assertEqual(3, len(programs))

            for journal_article in xml.findall(".//journal_article"):
                with self.subTest(journal_article=journal_article):
                    program = journal_article.findall(
                        ".//{http://www.crossref.org/AccessIndicators.xsd}program"
                    )
                    self.assertIsNotNone(program)
                    self.assertEqual(1, len(program))
                    self.assertEqual(
                        3,
                        len(
                            program[0].findall(
                                "{http://www.crossref.org/AccessIndicators.xsd}license_ref"
                            )
                        ),
                    )
                    self.assertIsNotNone(
                        program[0].findall(
                            "{http://www.crossref.org/AccessIndicators.xsd}free_to_read"
                        )
                    )


    def test_journal_article_should_not_contain_licenses(self):
            xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
                ["pt", "en", "es"]
            )

            data = [self._article_meta, xmlcrossref]
            xmlcrossref = export_crossref.XMLPermissionsPipe()
            _, xml = xmlcrossref.transform(data)

            programs = xml.findall(
                ".//{http://www.crossref.org/AccessIndicators.xsd}program"
            )

            self.assertIsNotNone(programs)


    def test_date_pipe_should_includes_year_when_it_is_valid(self):
        doi_batch = create_xmlcrossref_with_n_journal_article_element(["pt"])
        self._raw_json["citations"] = [{"v65": [{"_": "20060320"}]}]
        article_json = Article(self._raw_json)
        data = [article_json, doi_batch]

        xmlcrossref = export_crossref.XMLArticleCitationsPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertIsNotNone(xml.find(".//citation"))  # ensure citation

        expected_c_year = xml.find(".//cYear")

        self.assertIsNotNone(expected_c_year)
        self.assertEqual(u"2006", expected_c_year.text)

    def test_date_pipe_should_not_includes_year_when_it_is_zero(self):
        doi_batch = create_xmlcrossref_with_n_journal_article_element(["pt"])
        self._raw_json["citations"] = [{"v65": [{"_": "0000"}]}]
        article_json = Article(self._raw_json)
        data = [article_json, doi_batch]

        xmlcrossref = export_crossref.XMLArticleCitationsPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertIsNotNone(xml.find(".//citation"))  # ensure citation

        not_expected_c_year = xml.find(".//cYear")

        self.assertIsNone(not_expected_c_year)

class ExportCrossRef_MultiLingueDoc_with_MultipleDOI_Tests(unittest.TestCase):

    def setUp(self):
        article_json = {
            "fulltexts": {
                "pdf": {
                    "es": "http://www.scielo.br/pdf/rsp/v44n4/es_07.pdf",
                    "en": "http://www.scielo.br/pdf/rsp/v44n4/en_07.pdf",
                    "pt": "http://www.scielo.br/pdf/rsp/v44n4/07.pdf"
                },
                "html": {
                    "es": "http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0034-89102010000400007&tlng=es",
                    "en": "http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0034-89102010000400007&tlng=en",
                    "pt": "http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0034-89102010000400007&tlng=pt"
                }
            },
            "collection": "scl",
            "doi": "10.1590/S0034-89102010000400007",
            "body": {
                "pt": "Body PT",
                "es": "Body ES",
                "en": "Body EN"
            },
            "article": {
                "v880": [
                    {
                        "_": "S0034-89102010000400007"
                    }
                ],
                "v237": [
                    {
                        "_": "10.1590/S0034-89102010000400007"
                    }
                ],
                "v223": [
                    {
                        "_": "20100801"
                    }
                ],
                "v65": [
                    {
                        "_": "2010"
                    }
                ],
                "v601": [
                    {
                        "_": "en"
                    },
                    {
                        "_": "es"
                    },
                ],
                "v40": [
                    {
                        "_": "pt"
                    }
                ],
                "v10": [
                    {
                        "s": "Bamgboye",
                        "r": "ND",
                        "_": "",
                        "n": "EL"
                    }
                ],
                "v14": [
                    {
                        "f": "14",
                        "l": "20",
                    }
                ],
                "v12": [
                    {
                        "l": "pt",
                        "_": "Perfil epidemiológico dos pacientes em terapia"
                        " renal substitutiva no Brasil, 2000-2004"
                    },
                    {
                        "l": "en",
                        "_": "Epidemiological profile of patients on"
                        " renal replacement therapy in Brazil, 2000-2004"
                    },
                    {
                        "l": "es",
                        "_": "Perfil epidemiológico de los pacientes en terapia"
                        " renal substitutiva en Brasil, 2000-2004"
                    }
                ],
                "v337": [
                    {
                        "l": "pt",
                        "d": "10.1590/S0034-89102010000400007",
                    },
                    {
                        "l": "en",
                        "d": "10.1590/ID.en"
                    },
                    {
                        "l": "es",
                        "d": "10.1590/ID.es"
                    }

                ],
                "v83": [
                    {
                        "a": "OBJETIVO: Descrever o perfil epidemiol\u00f3gico...",
                        "l": "pt",
                        "_": ""
                    },
                    {
                        "a": "OBJECTIVE: To describe the clinical and epidemiological profile...",
                        "l": "en",
                        "_": ""
                    },
                    {
                        "a": "OBJETIVO: Describir el perfil epidemiol\u00f3gico y cl\u00ednico...",
                        "l": "es",
                        "_": ""
                    }
                ]
            },
            "citations": [
                {
                    "v30": [
                        {
                            "_": "Ethn Dis."
                        }
                    ],
                    "v31": [
                        {
                            "_": "16"
                        }
                    ],
                    "v32": [
                        {
                            "s": "2",
                            "_": "2"
                        }
                    ],
                    "v118": [
                        {
                            "_": "1"
                        }
                    ],
                    "v12": [
                        {
                            "l": "en",
                            "_": "End-stage renal disease in sub-Saharan Africa."
                        }
                    ],
                    "v65": [
                        {
                            "_": "20060000"
                        }
                    ],
                    "v64": [
                        {
                            "_": "2006"
                        }
                    ],
                    "v14": [
                        {
                            "_": "2,5,9"
                        }
                    ],
                    "v880": [
                        {
                            "_": "S0034-8910201000040000700001"
                        }
                    ],
                    "v701": [
                        {
                            "_": "1"
                        }
                    ],
                    "v865": [
                        {
                            "_": "20100800"
                        }
                    ],
                    "v702": [
                        {
                            "_": "V:\\Scielo\\serial\\rsp\\v44n4\\markup\\07.htm"
                        }
                    ],
                    "v10": [
                        {
                            "s": "Bamgboye",
                            "r": "ND",
                            "_": "",
                            "n": "EL"
                        }
                    ]
                },
            ],
            "issue": {
                "issue": {},
            },
        }
        self._article = Article(article_json)

    def test_journal_article_element(self):
        xmlcrossref = ET.Element('doi_batch')
        body = ET.Element('body')
        body.append(ET.Element('journal'))
        xmlcrossref.append(body)

        data = [self._article, xmlcrossref]

        xmlcrossref = export_crossref.XMLJournalArticlePipe()
        raw, xml = xmlcrossref.transform(data)

        langs = ['pt', 'en', 'es']
        self.assertEqual(len(xml.findall('.//journal_article')), 3)
        for ja, lang in zip(
                xml.findall('.//journal_article'), langs):
            with self.subTest(lang):
                self.assertEqual(ja.get('language'), lang)

    def test_article_titles_element(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'en', 'es'])

        data = [self._article, xmlcrossref]

        xmlcrossref = export_crossref.XMLArticleTitlesPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(len(xml.findall('.//journal_article/titles')), 3)

    def test_article_title_element(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'en', 'es'], 'titles')

        data = [self._article, xmlcrossref]

        xmlcrossref = export_crossref.XMLArticleTitlePipe()
        raw, xml = xmlcrossref.transform(data)

        expected_titles = [
            'Perfil epidemiológico dos pacientes em terapia renal substitutiva no Brasil, 2000-2004',
            'Epidemiological profile of patients on renal replacement therapy in Brazil, 2000-2004',
            'Perfil epidemiológico de los pacientes en terapia renal substitutiva en Brasil, 2000-2004',
        ]
        expected_alt_titles = [
            'Epidemiological profile of patients on renal replacement therapy in Brazil, 2000-2004',
            'Perfil epidemiológico dos pacientes em terapia renal substitutiva no Brasil, 2000-2004',
            'Epidemiological profile of patients on renal replacement therapy in Brazil, 2000-2004',
        ]
        
        titles = [node.text for node in xml.findall(".//journal_article//title")]
        alt_titles = [node.text for node in xml.findall(".//journal_article//original_language_title")]

        self.assertEqual(expected_titles, titles)
        self.assertEqual(expected_alt_titles, alt_titles)

    def test_article_contributors_element(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'en', 'es'])

        data = [self._article, xmlcrossref]

        xmlcrossref = export_crossref.XMLArticleContributorsPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(
            3, len(xml.findall('.//journal_article')))
        self.assertEqual(
            3, len(xml.findall('.//journal_article/contributors')))

    def test_article_publication_date_element(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'en', 'es'])

        data = [self._article, xmlcrossref]

        xmlcrossref = export_crossref.XMLArticlePubDatePipe()
        raw, xml = xmlcrossref.transform(data)

        expected = b"""<doi_batch><body><journal>
            <journal_article publication_type="full_text">
                <publication_date media_type="online">
                    <month>08</month>
                    <year>2010</year></publication_date></journal_article>
            <journal_article publication_type="full_text">
                <publication_date media_type="online">
                    <month>08</month>
                    <year>2010</year></publication_date></journal_article>
            <journal_article publication_type="full_text">
                <publication_date media_type="online">
                    <month>08</month>
                    <year>2010</year></publication_date></journal_article>
            </journal></body></doi_batch>"""

        for i, pubdate in enumerate(
                xml.findall('.//journal_article//publication_date')):
            with self.subTest(label=i):
                self.assertEqual(pubdate.findtext('year'), '2010')
                self.assertEqual(pubdate.findtext('month'), None)
                self.assertEqual(pubdate.findtext('data'), None)

    def test_article_pages_element(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'en', 'es'])

        data = [self._article, xmlcrossref]

        xmlcrossref = export_crossref.XMLPagesPipe()
        raw, xml = xmlcrossref.transform(data)

        for i, node in enumerate(
                xml.findall('.//journal_article//pages')):
            with self.subTest(label=i):
                self.assertEqual(node.findtext('first_page'), '14')
                self.assertEqual(node.findtext('last_page'), '20')

    def test_article_pid_element(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'en', 'es'])

        data = [self._article, xmlcrossref]

        xmlcrossref = export_crossref.XMLPIDPipe()
        raw, xml = xmlcrossref.transform(data)

        for i, node in enumerate(
                xml.findall('.//journal_article//publisher_item')):
            with self.subTest(label=i):
                self.assertEqual(
                    node.findtext('identifier'),
                    'S0034-89102010000400007')

    def test_doi_data_elem_for_multilingue_document(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'en', 'es'])

        data = [self._article, xmlcrossref]
        xmlcrossref = export_crossref.XMLDOIDataPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(
            3, len(xml.findall('.//journal_article')))
        self.assertEqual(
            3, len(xml.findall('.//doi_data')))

    def test_doi_elem_for_multilingue_document(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'en', 'es'], 'doi_data')

        data = [self._article, xmlcrossref]
        xmlcrossref = export_crossref.XMLDOIPipe()
        raw, xml = xmlcrossref.transform(data)

        expected_content = [
            ('10.1590/S0034-89102010000400007', 0),
            ('10.1590/ID.en', 1),
            ('10.1590/ID.es', 2),
        ]
        self.assertEqual(
            3, len(xml.findall('.//journal_article')))
        self.assertEqual(
            3, len(xml.findall('.//doi_data/doi')))

        for doi, content in zip(
                xml.findall('.//doi_data/doi'), expected_content):
            with self.subTest(label=content[1]):
                self.assertEqual(content[0], doi.text)

    def test_resource_elem_for_multilingue_document(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'en', 'es'], 'doi_data')

        data = [self._article, xmlcrossref]
        xmlcrossref = export_crossref.XMLResourcePipe()
        raw, xml = xmlcrossref.transform(data)

        expected_content = [
            ("http://www.scielo.br/scielo.php?"
                "script=sci_arttext&pid="
             "S0034-89102010000400007&tlng=pt", 0),
            ("http://www.scielo.br/scielo.php?"
                "script=sci_arttext&pid="
             "S0034-89102010000400007&tlng=en", 1),
            ("http://www.scielo.br/scielo.php?"
                "script=sci_arttext&pid="
             "S0034-89102010000400007&tlng=es", 2),
        ]
        self.assertEqual(
            3, len(xml.findall('.//journal_article')))
        self.assertEqual(
            3, len(xml.findall('.//doi_data/resource')))

        for resource, content in zip(
                xml.findall('.//doi_data/resource'), expected_content):
            with self.subTest(label=content[1]):
                self.assertEqual(content[0], resource.text)

    def test_article_abstracts_elem_for_multilingue_document(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'en', 'es'], 'doi_data')

        data = [self._article, xmlcrossref]
        xmlcrossref = export_crossref.XMLArticleAbstractPipe()
        raw, xml = xmlcrossref.transform(data)

        expected_abstracts = [
            "OBJETIVO: Descrever o perfil epidemiol\u00f3gico...",
            "OBJECTIVE: To describe the clinical and epidemiological profile...",
            "OBJETIVO: Describir el perfil epidemiol\u00f3gico y cl\u00ednico...",
            "OBJECTIVE: To describe the clinical and epidemiological profile...",
            "OBJETIVO: Descrever o perfil epidemiol\u00f3gico...",
            "OBJETIVO: Describir el perfil epidemiol\u00f3gico y cl\u00ednico...",
            "OBJETIVO: Describir el perfil epidemiol\u00f3gico y cl\u00ednico...",
            "OBJETIVO: Descrever o perfil epidemiol\u00f3gico...",
            "OBJECTIVE: To describe the clinical and epidemiological profile...",
        ]

        abstract_nodes = xml.findall(
            './/{http://www.ncbi.nlm.nih.gov/JATS1}abstract/{http://www.ncbi.nlm.nih.gov/JATS1}p')
        self.assertEqual(3, len(xml.findall('.//journal_article')))
        self.assertEqual(9, len(abstract_nodes))

        xml_abstracts = [a.text for a in abstract_nodes]
        print(xml_abstracts)
        self.assertListEqual(expected_abstracts, xml_abstracts)

    def test_related_item_for_multilingue_document(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'en', 'es'])

        data = [self._article, xmlcrossref]
        xmlcrossref = export_crossref.XMLProgramRelatedItemPipe()
        raw, xml = xmlcrossref.transform(data)

        expected_content = [
            ('10.1590/ID.en',
             "Epidemiological profile of patients on"
             " renal replacement therapy in Brazil, 2000-2004",
             0,
             "isTranslationOf",
             ),
            ('10.1590/ID.es',
             "Perfil epidemiológico de los pacientes en terapia"
             " renal substitutiva en Brasil, 2000-2004",
             1,
             "isTranslationOf",
             ),
            ('10.1590/S0034-89102010000400007',
             "Perfil epidemiológico dos pacientes em terapia"
             " renal substitutiva no Brasil, 2000-2004",
             2,
             "hasTranslation",
             ),
            ('10.1590/S0034-89102010000400007',
             "Perfil epidemiológico dos pacientes em terapia"
             " renal substitutiva no Brasil, 2000-2004",
             3,
             "hasTranslation",
             ),
        ]
        self.assertEqual(
            3, len(xml.findall('.//program')))
        self.assertEqual(
            4, len(xml.findall('.//program/related_item/intra_work_relation')))
        self.assertEqual(
            4, len(xml.findall('.//program/related_item/description')))

        for related_item, content in zip(
                xml.findall('.//program/related_item'), expected_content):
            with self.subTest(label=content[2]):
                self.assertEqual(
                    content[1], related_item.findtext('description'))
                intra_work_relation = related_item.find('intra_work_relation')
                self.assertEqual(
                    content[0], intra_work_relation.text)
                self.assertEqual(
                    'doi', intra_work_relation.attrib.get('identifier-type'))
                self.assertEqual(
                    content[3],
                    intra_work_relation.attrib.get('relationship-type'))

    def test_collection_for_multilingue_document(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'en', 'es'], 'doi_data')

        data = [self._article, xmlcrossref]
        xmlcrossref = export_crossref.XMLCollectionPipe()
        raw, xml = xmlcrossref.transform(data)

        texts = [
            "http://www.scielo.br/scielo.php?script=sci_pdf&pid=S0034-89102010000400007&tlng=pt",
            "http://www.scielo.br/scielo.php?script=sci_pdf&pid=S0034-89102010000400007&tlng=en",
            "http://www.scielo.br/scielo.php?script=sci_pdf&pid=S0034-89102010000400007&tlng=es",
        ]
        self.assertEqual(
            3, len(xml.findall('.//doi_data//collection')))
        for res, text in zip(
                xml.findall('.//doi_data/collection/item/resource'), texts):
            with self.subTest(text):
                self.assertEqual(res.text, text)

    def test_citations_for_multilingue_document(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'en', 'es'])

        data = [self._article, xmlcrossref]
        xmlcrossref = export_crossref.XMLArticleCitationsPipe()
        raw, xml = xmlcrossref.transform(data)
        self.assertEqual(
            3, len(xml.findall('.//journal_article//citation_list')))


    def test_every_journal_article_must_contain_own_license(self):
            self._article.data["license"] = "by/4.0"

            xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
                ["pt", "en", "es"]
            )

            data = [self._article, xmlcrossref]
            xmlcrossref = export_crossref.XMLPermissionsPipe()
            _, xml = xmlcrossref.transform(data)

            programs = xml.findall(
                ".//{http://www.crossref.org/AccessIndicators.xsd}program"
            )
            self.assertEqual(3, len(programs))

            for journal_article in xml.findall(".//journal_article"):
                with self.subTest(journal_article=journal_article):
                    program = journal_article.findall(
                        ".//{http://www.crossref.org/AccessIndicators.xsd}program"
                    )
                    self.assertIsNotNone(program)
                    self.assertEqual(1, len(program))
                    self.assertEqual(
                        3,
                        len(
                            program[0].findall(
                                "{http://www.crossref.org/AccessIndicators.xsd}license_ref"
                            )
                        ),
                    )
                    self.assertIsNotNone(
                        program[0].findall(
                            "{http://www.crossref.org/AccessIndicators.xsd}free_to_read"
                        )
                    )


    def test_journal_article_should_not_contain_licenses(self):
            xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
                ["pt", "en", "es"]
            )

            data = [self._article, xmlcrossref]
            xmlcrossref = export_crossref.XMLPermissionsPipe()
            _, xml = xmlcrossref.transform(data)

            programs = xml.findall(
                ".//{http://www.crossref.org/AccessIndicators.xsd}program"
            )

            self.assertIsNotNone(programs)


class ExportCrossRef_MultiLingueDoc_with_DOI_pt_es_Tests(unittest.TestCase):

    def setUp(self):
        article_json = {
            "fulltexts": {
                "pdf": {
                    "es": "http://www.scielo.br/pdf/rsp/v44n4/es_07.pdf",
                    "en": "http://www.scielo.br/pdf/rsp/v44n4/en_07.pdf",
                    "pt": "http://www.scielo.br/pdf/rsp/v44n4/07.pdf"
                },
                "html": {
                    "es": "http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0034-89102010000400007&tlng=es",
                    "en": "http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0034-89102010000400007&tlng=en",
                    "pt": "http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0034-89102010000400007&tlng=pt"
                }
            },
            "collection": "scl",
            "doi": "10.1590/S0034-89102010000400007",
            "body": {
                "pt": "Body PT",
                "es": "Body ES",
                "en": "Body EN"
            },
            "article": {
                "v880": [
                    {
                        "_": "S0034-89102010000400007"
                    }
                ],
                "v237": [
                    {
                        "_": "10.1590/S0034-89102010000400007"
                    }
                ],
                "v223": [
                    {
                        "_": "20100801"
                    }
                ],
                "v65": [
                    {
                        "_": "2010"
                    }
                ],
                "v601": [
                    {
                        "_": "en"
                    },
                    {
                        "_": "es"
                    },
                ],
                "v40": [
                    {
                        "_": "pt"
                    }
                ],
                "v10": [
                    {
                        "s": "Bamgboye",
                        "r": "ND",
                        "_": "",
                        "n": "EL"
                    }
                ],
                "v14": [
                    {
                        "f": "14",
                        "l": "20",
                    }
                ],
                "v12": [
                    {
                        "l": "pt",
                        "_": "Perfil epidemiológico dos pacientes em terapia"
                        " renal substitutiva no Brasil, 2000-2004"
                    },
                    {
                        "l": "en",
                        "_": "Epidemiological profile of patients on"
                        " renal replacement therapy in Brazil, 2000-2004"
                    },
                    {
                        "l": "es",
                        "_": "Perfil epidemiológico de los pacientes en terapia"
                        " renal substitutiva en Brasil, 2000-2004"
                    }
                ],
                "v337": [
                    {
                        "l": "pt",
                        "d": "10.1590/S0034-89102010000400007",
                    },
                    {
                        "l": "es",
                        "d": "10.1590/ID.es"
                    }

                ],
                "v83": [
                    {
                        "a": "OBJETIVO: Descrever o perfil epidemiol\u00f3gico...",
                        "l": "pt",
                        "_": ""
                    },
                    {
                        "a": "OBJECTIVE: To describe the clinical and epidemiological profile...",
                        "l": "en",
                        "_": ""
                    },
                    {
                        "a": "OBJETIVO: Describir el perfil epidemiol\u00f3gico y cl\u00ednico...",
                        "l": "es",
                        "_": ""
                    }
                ]
            },
            "citations": [
                {
                    "v30": [
                        {
                            "_": "Ethn Dis."
                        }
                    ],
                    "v31": [
                        {
                            "_": "16"
                        }
                    ],
                    "v32": [
                        {
                            "s": "2",
                            "_": "2"
                        }
                    ],
                    "v118": [
                        {
                            "_": "1"
                        }
                    ],
                    "v12": [
                        {
                            "l": "en",
                            "_": "End-stage renal disease in sub-Saharan Africa."
                        }
                    ],
                    "v65": [
                        {
                            "_": "20060000"
                        }
                    ],
                    "v64": [
                        {
                            "_": "2006"
                        }
                    ],
                    "v14": [
                        {
                            "_": "2,5,9"
                        }
                    ],
                    "v880": [
                        {
                            "_": "S0034-8910201000040000700001"
                        }
                    ],
                    "v701": [
                        {
                            "_": "1"
                        }
                    ],
                    "v865": [
                        {
                            "_": "20100800"
                        }
                    ],
                    "v702": [
                        {
                            "_": "V:\\Scielo\\serial\\rsp\\v44n4\\markup\\07.htm"
                        }
                    ],
                    "v10": [
                        {
                            "s": "Bamgboye",
                            "r": "ND",
                            "_": "",
                            "n": "EL"
                        }
                    ]
                },
            ],
            "issue": {
                "issue": {},
            },
        }
        self._article = Article(article_json)

    def test_journal_article_element(self):
        xmlcrossref = ET.Element('doi_batch')
        body = ET.Element('body')
        body.append(ET.Element('journal'))
        xmlcrossref.append(body)

        data = [self._article, xmlcrossref]

        xmlcrossref = export_crossref.XMLJournalArticlePipe()
        raw, xml = xmlcrossref.transform(data)

        langs = ['pt', 'es']
        self.assertEqual(len(xml.findall('.//journal_article')), 2)
        for ja, lang in zip(
                xml.findall('.//journal_article'), langs):
            with self.subTest(lang):
                self.assertEqual(ja.get('language'), lang)

    def test_article_titles_element(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'es'])

        data = [self._article, xmlcrossref]

        xmlcrossref = export_crossref.XMLArticleTitlesPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(len(xml.findall('.//journal_article/titles')), 2)

    def test_article_title_element(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'es'], 'titles')

        self._article.data["article"]["v12"] = [
            {
                "l": "pt",
                "_": "Perfil epidemiológico dos pacientes em terapia"
                " renal substitutiva no Brasil, 2000-2004"
            },
            {
                "l": "es",
                "_": "Perfil epidemiológico de los pacientes en terapia"
                " renal substitutiva en Brasil, 2000-2004"
            }
        ]
        data = [self._article, xmlcrossref]

        xmlcrossref = export_crossref.XMLArticleTitlePipe()
        raw, xml = xmlcrossref.transform(data)

        expected_titles = [
            'Perfil epidemiológico dos pacientes em terapia renal substitutiva no Brasil, 2000-2004',
            'Perfil epidemiológico de los pacientes en terapia renal substitutiva en Brasil, 2000-2004',
        ]
        expected_alt_titles = [
            'Perfil epidemiológico de los pacientes en terapia renal substitutiva en Brasil, 2000-2004',
            'Perfil epidemiológico dos pacientes em terapia renal substitutiva no Brasil, 2000-2004',
        ]
        titles = [node.text for node in xml.findall(".//journal_article//title")]
        alt_titles = [node.text for node in xml.findall(".//journal_article//original_language_title")]

        self.assertEqual(expected_titles, titles)
        self.assertEqual(expected_alt_titles, alt_titles)

    def test_article_title_element_once(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt'], 'titles')

        self._article.data["article"]["v12"] = [
            {
                "l": "pt",
                "_": "Perfil epidemiológico dos pacientes em terapia"
                " renal substitutiva no Brasil, 2000-2004"
            },
        ]
        data = [self._article, xmlcrossref]

        xmlcrossref = export_crossref.XMLArticleTitlePipe()
        raw, xml = xmlcrossref.transform(data)

        expected_titles = [
            'Perfil epidemiológico dos pacientes em terapia renal substitutiva no Brasil, 2000-2004',
        ]
        expected_alt_titles = []
        titles = [node.text for node in xml.findall(".//journal_article//title")]
        alt_titles = [node.text for node in xml.findall(".//journal_article//original_language_title")]

        self.assertEqual(expected_titles, titles)
        self.assertEqual(expected_alt_titles, alt_titles)

    def test_article_contributors_element(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'es'])

        data = [self._article, xmlcrossref]

        xmlcrossref = export_crossref.XMLArticleContributorsPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(
            2, len(xml.findall('.//journal_article')))
        self.assertEqual(
            2, len(xml.findall('.//journal_article/contributors')))

    def test_article_publication_date_element(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'es'])

        data = [self._article, xmlcrossref]

        xmlcrossref = export_crossref.XMLArticlePubDatePipe()
        raw, xml = xmlcrossref.transform(data)
        self.assertEqual(
            2, len(xml.findall('.//journal_article//publication_date')))
        for i, pubdate in enumerate(
                xml.findall('.//journal_article//publication_date')):
            with self.subTest(label=i):
                self.assertEqual(pubdate.findtext('year'), '2010')
                self.assertEqual(pubdate.findtext('month'), None)
                self.assertEqual(pubdate.findtext('data'), None)

    def test_article_pages_element(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'es'])

        data = [self._article, xmlcrossref]

        xmlcrossref = export_crossref.XMLPagesPipe()
        raw, xml = xmlcrossref.transform(data)
        self.assertEqual(
            2, len(xml.findall('.//journal_article//pages')))
        for i, node in enumerate(
                xml.findall('.//journal_article//pages')):
            with self.subTest(label=i):
                self.assertEqual(node.findtext('first_page'), '14')
                self.assertEqual(node.findtext('last_page'), '20')

    def test_article_pid_element(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'es'])

        data = [self._article, xmlcrossref]

        xmlcrossref = export_crossref.XMLPIDPipe()
        raw, xml = xmlcrossref.transform(data)
        self.assertEqual(
            2, len(xml.findall('.//journal_article//publisher_item')))
        for i, node in enumerate(
                xml.findall('.//journal_article//publisher_item')):
            with self.subTest(label=i):
                self.assertEqual(
                    node.findtext('identifier'),
                    'S0034-89102010000400007')

    def test_doi_data_elem_for_multilingue_document(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'es'])

        data = [self._article, xmlcrossref]
        xmlcrossref = export_crossref.XMLDOIDataPipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(
            2, len(xml.findall('.//journal_article')))
        self.assertEqual(
            2, len(xml.findall('.//doi_data')))

    def test_doi_elem_for_multilingue_document(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'es'], 'doi_data')

        data = [self._article, xmlcrossref]
        xmlcrossref = export_crossref.XMLDOIPipe()
        raw, xml = xmlcrossref.transform(data)

        expected_content = [
            ('10.1590/S0034-89102010000400007', 0),
            ('10.1590/ID.es', 2),
        ]
        self.assertEqual(
            2, len(xml.findall('.//journal_article')))
        self.assertEqual(
            2, len(xml.findall('.//doi_data/doi')))

        for doi, content in zip(
                xml.findall('.//doi_data/doi'), expected_content):
            with self.subTest(label=content[1]):
                self.assertEqual(content[0], doi.text)

    def test_resource_elem_for_multilingue_document(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'es'], 'doi_data')

        data = [self._article, xmlcrossref]
        xmlcrossref = export_crossref.XMLResourcePipe()
        raw, xml = xmlcrossref.transform(data)

        expected_content = [
            ("http://www.scielo.br/scielo.php?"
                "script=sci_arttext&pid="
             "S0034-89102010000400007&tlng=pt", 0),
            ("http://www.scielo.br/scielo.php?"
                "script=sci_arttext&pid="
             "S0034-89102010000400007&tlng=es", 2),
        ]
        self.assertEqual(
            2, len(xml.findall('.//journal_article')))
        self.assertEqual(
            2, len(xml.findall('.//doi_data/resource')))

        for resource, content in zip(
                xml.findall('.//doi_data/resource'), expected_content):
            with self.subTest(label=content[1]):
                self.assertEqual(content[0], resource.text)

    def test_article_abstracts_elem_for_multilingue_document(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'es'], 'doi_data')

        data = [self._article, xmlcrossref]
        xmlcrossref = export_crossref.XMLArticleAbstractPipe()
        raw, xml = xmlcrossref.transform(data)

        expected_abstracts = [
            "OBJETIVO: Descrever o perfil epidemiol\u00f3gico...",
            "OBJECTIVE: To describe the clinical and epidemiological profile...",
            "OBJETIVO: Describir el perfil epidemiol\u00f3gico y cl\u00ednico...",
            "OBJETIVO: Describir el perfil epidemiol\u00f3gico y cl\u00ednico...",
            "OBJETIVO: Descrever o perfil epidemiol\u00f3gico...",
            "OBJECTIVE: To describe the clinical and epidemiological profile...",
        ]

        abstract_nodes = xml.findall(
            './/{http://www.ncbi.nlm.nih.gov/JATS1}abstract/{http://www.ncbi.nlm.nih.gov/JATS1}p')
        self.assertEqual(2, len(xml.findall('.//journal_article')))
        self.assertEqual(6, len(abstract_nodes))

        xml_abstracts = [a.text for a in abstract_nodes]
        self.assertEqual(expected_abstracts, xml_abstracts)

    def test_related_item_for_multilingue_document(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'es'])

        data = [self._article, xmlcrossref]
        xmlcrossref = export_crossref.XMLProgramRelatedItemPipe()
        raw, xml = xmlcrossref.transform(data)

        expected_content = [
            ('10.1590/ID.es',
             "Perfil epidemiológico de los pacientes en terapia"
             " renal substitutiva en Brasil, 2000-2004",
             0,
             "isTranslationOf",
             ),
            ('10.1590/S0034-89102010000400007',
             "Perfil epidemiológico dos pacientes em terapia"
             " renal substitutiva no Brasil, 2000-2004",
             1,
             "hasTranslation",
             ),
        ]
        self.assertEqual(
            2, len(xml.findall('.//program')))
        self.assertEqual(
            2, len(xml.findall('.//program/related_item/intra_work_relation')))
        self.assertEqual(
            2, len(xml.findall('.//program/related_item/description')))

        for related_item, content in zip(
                xml.findall('.//program/related_item'), expected_content):
            with self.subTest(label=content[2]):
                self.assertEqual(
                    content[1], related_item.findtext('description'))
                intra_work_relation = related_item.find('intra_work_relation')
                self.assertEqual(
                    content[0], intra_work_relation.text)
                self.assertEqual(
                    'doi', intra_work_relation.attrib.get('identifier-type'))
                self.assertEqual(
                    content[3],
                    intra_work_relation.attrib.get('relationship-type'))

    def test_collection_for_multilingue_document(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'es'], 'doi_data')

        data = [self._article, xmlcrossref]
        xmlcrossref = export_crossref.XMLCollectionPipe()
        raw, xml = xmlcrossref.transform(data)

        texts = [
            "http://www.scielo.br/scielo.php?script=sci_pdf&pid=S0034-89102010000400007&tlng=pt",
            "http://www.scielo.br/scielo.php?script=sci_pdf&pid=S0034-89102010000400007&tlng=es",
        ]

        self.assertEqual(
            2, len(xml.findall('.//doi_data//collection')))
        for res, text in zip(
                xml.findall('.//doi_data/collection/item/resource'), texts):
            with self.subTest(text):
                self.assertEqual(res.text, text)

    def test_citations_for_multilingue_document(self):
        xmlcrossref = create_xmlcrossref_with_n_journal_article_element(
            ['pt', 'es'])

        data = [self._article, xmlcrossref]
        xmlcrossref = export_crossref.XMLArticleCitationsPipe()
        raw, xml = xmlcrossref.transform(data)
        self.assertEqual(
            2, len(xml.findall('.//journal_article//citation_list')))


class ExportCrossRef_XMLArticlePubDatePipe_Tests(unittest.TestCase):

    def setUp(self):
        self.xmlcrossref = ET.Element('doi_batch')
        journal_article = ET.Element('journal_article')
        journal_article.set('publication_type', 'full_text')
        journal = ET.Element('journal')
        journal.append(journal_article)
        body = ET.Element('body')
        body.append(journal)
        self.xmlcrossref.append(body)

    def test_article_publication_date_element_aop_article(self):
        _raw_json = {
            'issue': {
                'issue': {'v32': [{'_': 'ahead'}]},
             },
            'article': {
                'v32': [{'_': 'ahead'}],
                'v223': [{'_': '20190325'}],
            },
        }
        _article = Article(_raw_json)
        data = [_article, self.xmlcrossref]

        xmlcrossref = export_crossref.XMLArticlePubDatePipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(
            b'<doi_batch><body><journal><journal_article publication_type="full_text"><publication_date media_type="online"><month>03</month><day>25</day><year>2019</year></publication_date></journal_article></journal></body></doi_batch>',
            ET.tostring(xml)
        )

    def test_article_publication_date_element_issue_article(self):
        _raw_json = {
            'issue': {
                'issue': {'v32': [{'_': '10'}]},
            },
            'article': {
                'v32': [{'_': '10'}],
                'v65': [{'_': '20190300'}],
            },
        }
        _article = Article(_raw_json)
        data = [_article, self.xmlcrossref]

        xmlcrossref = export_crossref.XMLArticlePubDatePipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(
            b'<doi_batch><body><journal><journal_article publication_type="full_text"><publication_date media_type="online"><month>03</month><year>2019</year></publication_date></journal_article></journal></body></doi_batch>',
            ET.tostring(xml)
        )

    def test_article_publication_date_element_continuospub_article(self):
        _raw_json = {
            'issue': {
                'issue': {'v32': [{'_': '10'}]},
            },
            'article': {
                'v32': [{'_': '10'}],
                'v65': [{'_': '20190000'}],
            },
        }
        _article = Article(_raw_json)
        data = [_article, self.xmlcrossref]

        xmlcrossref = export_crossref.XMLArticlePubDatePipe()
        raw, xml = xmlcrossref.transform(data)

        self.assertEqual(
            b'<doi_batch><body><journal><journal_article publication_type="full_text"><publication_date media_type="online"><year>2019</year></publication_date></journal_article></journal></body></doi_batch>',
            ET.tostring(xml)
        )


class ExportCrossRef_XMLIssuePipe_Tests(unittest.TestCase):

    def setUp(self):
        self.xmlcrossref = ET.Element('doi_batch')
        journal = ET.Element('journal')
        journal.append(ET.Element('journal_issue'))
        body = ET.Element('body')
        body.append(journal)
        self.xmlcrossref.append(body)

    def test_aop_element(self):
        _raw_json = {
            'issue':
                {'issue':
                    {'v32': [{'_': 'ahead'}]},
                 },
            'article':
                {'v32': [{'_': 'ahead'}]},
            }
        _article = Article(_raw_json)

        data = [_article, self.xmlcrossref]

        _xmlcrossref = export_crossref.XMLIssuePipe()
        raw, xml = _xmlcrossref.transform(data)

        self.assertEqual(xml.find('.//journal_issue/issue'), None)
        self.assertEqual(
            b'<doi_batch><body><journal><journal_issue/></journal></body></doi_batch>',
            ET.tostring(xml))

    def test_issue_element(self):
        _raw_json = {
            'issue':
                {'issue':
                    {'v32': [{'_': '10'}]},
                 },
            'article':
                {'v32': [{'_': '10'}]},
            }
        _article = Article(_raw_json)

        data = [_article, self.xmlcrossref]

        _xmlcrossref = export_crossref.XMLIssuePipe()
        raw, xml = _xmlcrossref.transform(data)

        self.assertEqual(xml.findtext('.//journal_issue/issue'), '10')
        self.assertEqual(
            b'<doi_batch><body><journal><journal_issue><issue>10</issue></journal_issue></journal></body></doi_batch>',
            ET.tostring(xml))


class ExportCrossRef_XMLVolumePipe_Tests(unittest.TestCase):

    def setUp(self):
        self.xmlcrossref = ET.Element('doi_batch')
        journal = ET.Element('journal')
        journal.append(ET.Element('journal_issue'))
        body = ET.Element('body')
        body.append(journal)
        self.xmlcrossref.append(body)

    def test_aop_element(self):
        _raw_json = {
            'issue':
                {'issue':
                    {'v32': [{'_': 'ahead'}]},
                 },
            'article':
                {'v32': [{'_': 'ahead'}]},
            }
        _article = Article(_raw_json)
        data = [_article, self.xmlcrossref]

        _xmlcrossref = export_crossref.XMLVolumePipe()
        raw, xml = _xmlcrossref.transform(data)
        self.assertEqual(
            b'<doi_batch><body><journal><journal_issue/></journal></body></doi_batch>',
            ET.tostring(xml))

class ExportCrossRef_XMLFundingData_Tests(unittest.TestCase):
    def setUp(self):
        namespace_map = {
            "xsi": "http://www.w3.org/2001/XMLSchema-instance",
            "jats": "http://www.ncbi.nlm.nih.gov/JATS1",
            "ai": "http://www.crossref.org/AccessIndicators.xsd",
            "fr": "http://www.crossref.org/fundref.xsd",
        }

        ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")
        ET.register_namespace('jats', "http://www.ncbi.nlm.nih.gov/JATS1")
        ET.register_namespace('ai', "http://www.crossref.org/AccessIndicators.xsd")
        ET.register_namespace('fr', "http://www.crossref.org/fundref.xsd")

        self.xmlcrossref =  ET.Element(
            '{http://www.crossref.org/schema/4.4.0}doi_batch',
            nsmap=namespace_map,
            attrib={
                '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation': (
                    "http://www.crossref.org/schema/4.4.0 "
                    "http://www.crossref.org/schemas/crossref4.4.0.xsd"
                ),
                'version': '4.4.0'
            }
        )
        journal = ET.Element('journal')
        journal_article = ET.Element('journal_article')
        publisher_item = ET.Element('publisher_item')
        xxx = ET.Element('xxx')
        body = ET.Element('body')

        journal_article.append(publisher_item)
        journal_article.append(xxx)
        journal.append(journal_article)
        
        body.append(journal)
        self.xmlcrossref.append(body)

    def test_funding_data_element(self):
        _raw_json = {
            'article':
                {
                    'v58': [
                        {
                            "_": "CNPQ"
                        },
                        {
                            "_": "Ministério da Saúde"
                        }
                    ],
                    'v60': [
                        {
                            "_": "nº 308051/2022-0-CNPQ"
                        },
                        {
                            "_": "nº 18/2020"
                        }
                    ],
                },
            }
        _article = Article(_raw_json)
        data = [_article, self.xmlcrossref]

        _xmlcrossref = export_crossref.XMLFundingDataPipe()
        raw, xml = _xmlcrossref.transform(data)
        
        publisher_item = xml.xpath(".//journal_article/publisher_item")[-1]

        self.assertEqual(publisher_item.getnext().find("*").tag, "{http://www.crossref.org/fundref.xsd}assertion")
        self.assertIn("fr:program", ET.tostring(xml).decode("utf-8"))