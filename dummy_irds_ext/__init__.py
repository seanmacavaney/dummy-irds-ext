import ir_datasets
from ir_datasets.formats import TsvDocs, TsvQueries, TrecQrels

NAME = 'macavaney:dummy'

QREL_DEFS = {
	1: 'relevant',
	0: 'not relevant',
}

DL_DOCS = ir_datasets.util.RequestsDownload('https://raw.githubusercontent.com/seanmacavaney/dummy-irds-ext/master/data/docs.tsv')
DL_QUERIES = ir_datasets.util.RequestsDownload('https://raw.githubusercontent.com/seanmacavaney/dummy-irds-ext/master/data/queries.tsv')
DL_QRELS = ir_datasets.util.RequestsDownload('https://raw.githubusercontent.com/seanmacavaney/dummy-irds-ext/master/data/qrels')

base_path = ir_datasets.util.home_path() / NAME

dataset = ir_datasets.Dataset(
	TsvDocs(ir_datasets.util.Cache(DL_DOCS, base_path/'docs.tsv')),
	TsvQueries(ir_datasets.util.Cache(DL_QUERIES, base_path/'queries.tsv')),
	TrecQrels(ir_datasets.util.Cache(DL_QRELS, base_path/'qrels'), QREL_DEFS),
)

ir_datasets.registry.register(NAME, dataset)
