{\rtf1\ansi\ansicpg1252\cocoartf1561\cocoasubrtf200
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;\f1\fnil\fcharset222 Ayuthaya;\f2\fnil\fcharset0 Roboto-Regular;
}
{\colortbl;\red255\green255\blue255;\red203\green35\blue57;\red255\green255\blue255;\red27\green31\blue34;
\red21\green23\blue26;\red87\green96\blue106;\red7\green68\blue184;\red6\green33\blue79;\red21\green23\blue25;
\red228\green234\blue239;\red91\green40\blue180;\red218\green76\blue12;}
{\*\expandedcolortbl;;\cssrgb\c84314\c22745\c28627;\cssrgb\c100000\c100000\c100000;\cssrgb\c14118\c16078\c18039;
\cssrgb\c10588\c12157\c13725\c29804;\cssrgb\c41569\c45098\c49020;\cssrgb\c0\c36078\c77255;\cssrgb\c1176\c18431\c38431;\cssrgb\c10588\c11765\c12941;
\cssrgb\c91373\c93333\c94902;\cssrgb\c43529\c25882\c75686;\cssrgb\c89020\c38431\c3529;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh15520\viewkind0
\deftab720

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrt\brdrnil \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clmgf \clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clmrg \clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
from\cf4  flask \cf2 import\cf4  Flask, request\cb1 \cell 
\pard\intbl\itap1\cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 \cb3 import\cf4  json\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 \cb3 import\cf4  requests\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3 \
\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf6 \cb3 # 
\f1 \'b5\'c3\'a7
\f0  YOURSECRETKEY 
\f1 \'b5\'e9\'cd\'a7\'b9\'d3\'c1\'d2\'e3\'ca\'e8\'e0\'cd\'a7\'a4\'c3\'d1\'ba\'a8\'d0\'a1\'c5\'e8\'d2\'c7\'b6\'d6\'a7\'e3\'b9\'a2\'d1\'e9\'b9\'b5\'cd\'b9\'b5\'e8\'cd\'e6
\f0  
\f1 \'e4\'bb
\f0 \cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 \cb3 global\cf4  \cf7 LINE_API_KEY\cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf7 \cb3 LINE_API_KEY\cf4  \cf2 =\cf4  \cf8 'Bearer 
\f2\fs28 \cf9 \cb10 a219910df8c362cffb8f3209bb1312c1
\f0\fs24 \cf8 \cb3 '\cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3 \
\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3 app \cf2 =\cf4  Flask(\cf7 __name__\cf4 )\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3  \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf11 \cb3 @app.route\cf4 (\cf8 '/'\cf4 )\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 \cb3 def\cf4  \cf11 index\cf4 ():\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 return\cf4  \cf8 'This is chatbot server.'\cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf11 \cb3 @app.route\cf4 (\cf8 '/bot'\cf4 , \cf12 methods\cf2 =\cf4 [\cf8 'POST'\cf4 ])\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3 \
\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 \cb3 def\cf4  \cf11 bot\cf4 ():\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf6 # 
\f1 \'a2\'e9\'cd\'a4\'c7\'d2\'c1\'b7\'d5\'e8\'b5\'e9\'cd\'a7\'a1\'d2\'c3\'ca\'e8\'a7\'a1\'c5\'d1\'ba
\f0 \cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     replyStack \cf2 =\cf4  \cf7 list\cf4 ()\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3    \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf6 # 
\f1 \'a2\'e9\'cd\'a4\'c7\'d2\'c1\'b7\'d5\'e8\'e4\'b4\'e9\'c3\'d1\'ba\'c1\'d2
\f0 \cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     msg_in_json \cf2 =\cf4  request.get_json()\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     msg_in_string \cf2 =\cf4  json.dumps(msg_in_json)\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf6 # Token 
\f1 \'ca\'d3\'cb\'c3\'d1\'ba\'b5\'cd\'ba\'a1\'c5\'d1\'ba
\f0  (
\f1 \'a8\'d3\'e0\'bb\'e7\'b9\'b5\'e9\'cd\'a7\'e3\'aa\'e9\'e3\'b9\'a1\'d2\'c3\'b5\'cd\'ba\'a1\'c5\'d1\'ba
\f0 )\cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     replyToken \cf2 =\cf4  msg_in_json[\cf8 "events"\cf4 ][\cf7 0\cf4 ][\cf8 'replyToken'\cf4 ]\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf6 # 
\f1 \'ca\'e8\'c7\'b9\'b9\'d5\'e9\'b4\'d6\'a7\'a2\'e9\'cd\'c1\'d9\'c5\'be\'d7\'e9\'b9\'b0\'d2\'b9\'cd\'cd\'a1\'c1\'d2\'a8\'d2\'a1
\f0  json (
\f1 \'e0\'bc\'d7\'e8\'cd
\f0 )\cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     userID \cf2 =\cf4   msg_in_json[\cf8 "events"\cf4 ][\cf7 0\cf4 ][\cf8 'source'\cf4 ][\cf8 'userId'\cf4 ]\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     msgType \cf2 =\cf4   msg_in_json[\cf8 "events"\cf4 ][\cf7 0\cf4 ][\cf8 'message'\cf4 ][\cf8 'type'\cf4 ]\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf6 # 
\f1 \'b5\'c3\'c7\'a8\'ca\'cd\'ba\'c7\'e8\'d2
\f0  
\f1 \'b7\'d5\'e8\'ca\'e8\'a7\'e0\'a2\'e9\'d2\'c1\'d2\'e0\'bb\'e7\'b9
\f0  text 
\f1 \'c3\'d6\'bb\'e8\'d2\'c7
\f0  (
\f1 \'cd\'d2\'a8\'e0\'bb\'e7\'b9
\f0  
\f1 \'c3\'d9\'bb
\f0 , location 
\f1 \'cd\'d0\'e4\'c3\'e1\'ba\'ba\'b9\'d5\'e9\'e4\'b4\'e9\'a4\'c3\'d1\'ba
\f0 )\cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf6 #if msgType != 'text':\cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf6 #    reply(replyToken, ['Only text is allowed.'])\cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf6 #    return 'OK',200\cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf6 # 
\f1 \'b5\'c3\'a7\'b9\'d5\'e9\'b5\'e9\'cd\'a7\'e1\'b9\'e8\'e3\'a8\'c7\'e8\'d2
\f0  msgType 
\f1 \'e0\'bb\'e7\'b9\'bb\'c3\'d0\'e0\'c0\'b7
\f0  text 
\f1 \'b6\'d6\'a7\'e0\'c3\'d5\'c2\'a1\'e4\'b4\'e9\'a4\'c3\'d1\'ba
\f0 \cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf6 #text = msg_in_json["events"][0]['message']['text'].lower().strip()\cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 if\cf4  msgType \cf2 !=\cf4  \cf8 'text'\cf4 :\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3         reply(replyToken, [\cf8 'Only text is allowed.'\cf4 ])\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3         \cf2 return\cf4  \cf8 'OK'\cf4 ,\cf7 200\cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     text \cf2 =\cf4  msg_in_json[\cf8 "events"\cf4 ][\cf7 0\cf4 ][\cf8 'message'\cf4 ][\cf8 'text'\cf4 ].lower().strip()\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3 \
\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf6 # 
\f1 \'b5\'cd\'ba\'a2\'e9\'cd\'a4\'c7\'d2\'c1
\f0  "
\f1 \'b9\'d5\'e8\'a4\'d7\'cd\'c3\'d9\'bb\'e1\'ba\'ba\'a2\'e9\'cd\'a4\'c7\'d2\'c1\'b7\'d5\'e8\'c3\'d1\'ba\'ca\'e8\'a7
\f0 " 
\f1 \'a1\'c5\'d1\'ba\'e4\'bb
\f0 \cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     replyStack.append(\cf8 '
\f1 \'b9\'d5\'e8\'a4\'d7\'cd\'c3\'d9\'bb\'e1\'ba\'ba\'a2\'e9\'cd\'a4\'c7\'d2\'c1\'b7\'d5\'e8\'c3\'d1\'ba\'ca\'e8\'a7
\f0 '\cf4 )\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf6 # 
\f1 \'b7\'b4\'c5\'cd\'a7
\f0  Echo 
\f1 \'a2\'e9\'cd\'a4\'c7\'d2\'c1\'a1\'c5\'d1\'ba\'e4\'bb\'e3\'b9\'c3\'d9\'bb\'e1\'ba\'ba\'b7\'d5\'e8\'ca\'e8\'a7\'e4\'bb\'c1\'d2
\f0  (
\f1 \'e1\'ba\'ba
\f0  json)\cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     replyStack.append(msg_in_string)\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     reply(replyToken, replyStack[:\cf7 5\cf4 ])\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 return\cf4  \cf8 'OK'\cf4 , \cf7 200\cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3  \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 \cb3 def\cf4  \cf11 reply\cf4 (replyToken, textList):\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf6 # Method 
\f1 \'ca\'d3\'cb\'c3\'d1\'ba\'b5\'cd\'ba\'a1\'c5\'d1\'ba\'a2\'e9\'cd\'a4\'c7\'d2\'c1\'bb\'c3\'d0\'e0\'c0\'b7
\f0  text 
\f1 \'a1\'c5\'d1\'ba\'a4\'c3\'d1\'ba
\f0  
\f1 \'e0\'a2\'d5\'c2\'b9\'e1\'ba\'ba\'b9\'d5\'e9\'e0\'c5\'c2\'a1\'e7\'e4\'b4\'e9\'a4\'c3\'d1\'ba
\f0 \cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf7 LINE_API\cf4  \cf2 =\cf4  \cf8 'https://api.line.me/v2/bot/message/reply'\cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     headers \cf2 =\cf4  \{\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3         \cf8 'Content-Type'\cf4 : \cf8 'application/json; charset=UTF-8'\cf4 ,\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3         \cf8 'Authorization'\cf4 : \cf7 LINE_API_KEY\cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \}\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     msgs \cf2 =\cf4  []\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 for\cf4  text \cf2 in\cf4  textList:\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3         msgs.append(\{\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3             \cf8 "type"\cf4 :\cf8 "text"\cf4 ,\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3             \cf8 "text"\cf4 :text\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3         \})\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     data \cf2 =\cf4  json.dumps(\{\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3         \cf8 "replyToken"\cf4 :replyToken,\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3         \cf8 "messages"\cf4 :msgs\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \})\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     requests.post(\cf7 LINE_API\cf4 , \cf12 headers\cf2 =\cf4 headers, \cf12 data\cf2 =\cf4 data)\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     \cf2 return\cf4 \cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3 \
\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 \cb3 if\cf4  \cf7 __name__\cf4  \cf2 ==\cf4  \cf8 '__main__'\cf4 :\cb1 \cell \row

\itap1\trowd \taflags1 \trgaph108\trleft-108 \trbrdrl\brdrnil \trbrdrt\brdrnil \trbrdrr\brdrnil 
\clvertalt \clshdrawnil \clwWidth289\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx4320
\clvertalt \clshdrawnil \clwWidth12870\clftsWidth3 \clbrdrt\brdrnil \clbrdrl\brdrnil \clbrdrb\brdrnil \clbrdrr\brdrnil \clpadt20 \clpadl200 \clpadb20 \clpadr200 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf5 \cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf4 \cb3     app.run()\cell \lastrow\row
}