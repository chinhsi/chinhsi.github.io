from scholarly import scholarly
import json
from datetime import datetime
import os

# Only fetch basic info and citation counts (much faster)
author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts'])
name = author['name']
author['updated'] = str(datetime.now())

# Print summary
print(f"Author: {name}")
print(f"Total citations: {author.get('citedby', 0)}")
print(f"h-index: {author.get('hindex', 0)}")
print(f"i10-index: {author.get('i10index', 0)}")
print(json.dumps(author, indent=2))

os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author.get('citedby', 0)}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

print("✓ Citation data updated successfully!")
