# dummy-irds-ext

A sample `ir_datasets` extension, adding a dummy dataset.

To use this with the python interface, you need to import it before calling `.load()`:

```python
import ir_datasets
import dummy_irds_ext
dataset = ir_datasets.load('macavaney:dummy')
for doc in dataset.iter_docs():
	...
```
