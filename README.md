# document-analyser
First attempt to build a text classifer for pdf documents using textblob

## How to use this
- clone the repository
- take any sample pdf file 
- ```pip3 install textblob PyPDF2```
- run the code using the following command ```python3 app.py -f sample.pdf```

#### Each sentence in the pdf is analysed as positive or negative

# Note
The accuracy will definitely be poor due to lack of dataset, please feel free to create a pull request to add more data or make changes :)

### License
```
Copyright 2020 Saiprasanth R.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.