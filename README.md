# What is it ?

This code adds the video IDs of youtube channels to the 'videoliste' table in the database.

![enter image description here](https://lh3.googleusercontent.com/ZRCvBV4Alih-jPZE9uw-s5H8PtdDQuV8yyrvJhPxMrTnhSM7ET4jAAiMifusTwEhMeb2aXHgI2mA_DOximSJnzYiTV1VZWG5zjLip2WC30PbHi5uOWNhSwGnTbPeWrhpdUO-wL1_JDGXGaBJ8WLF9sJsFJWGsqO6m1VB83aWpCnzndhyuBs1khxfA-El0v2zXWbuGJgrN30B5UMu4u5K3XaWMgHJcZc6LP6ud12yCcNGZxbboC03dR_zxPT6lcAq0ivlMi816gp45fFnaPxEfunLBQduRn-nAvq0O-SwstKqsD_cRBdBOM1wYEp_VEHjWyBp-j_12eLUlRDYq9Y7kH9nuZz44RAhv9ZrW13XD-_Rx51qJ8XLhNoFsOHSoRml9r7lcG-4NQckJVgHrA5QAYr6YQzLsy9ra-ZXNMsM64TtEhhCNbrxMbaAu4vnjnshYR3A30IWSnL07lUorqClc4C8J5V5KVQB_g_7mygd-_h_qYqnHp-oL7ppUn_TJJAKqwCX-KgSF-naLm4UlKpQVLtg9WtTbFoa9h-wG0dK5vYBdYsWgYo_YIQB4Vhd1EsppViYf0-JIKp6ofUfE4VhLv2krFG9BRMLJmvgru-NoZjzPQrwVxpnahSwZoStNYHw64QOOaK_H1DMlRc9ww-1cK6v9JckxtUo6Tdh_T_3BS5JFO8XGQEHlIk5WpMU=w381-h112-no?authuser=0)
# How does it work

  
To use the Youtube Data API service, you need to get an API_Key. You can get it from the address below.

 - [Console Cloud Google](https://console.cloud.google.com/)

 
In order for this code to work, there must be a table named 'kanal' in the database. Retrieves the 'kanal_ID' data from this table.

![enter image description here](https://lh3.googleusercontent.com/vGIg-58EdGlwncCY3ThV-o4dC4UFs28HiCNs-gxert9uU6wbyO8i9rJMdUAfmKhmL5md7uZCT-xDoDhJBKH4DUwRyr0D3tUvLwEbUOCWIXFB1rWV4gs9aE0Rx5TNfywAAgkq0Vn-MOii6AUYp0veRdLMJC8STO2KfRb6c5BYWX_VtcPNANElyRf54YjpJFOGYuUgb9r2bWRA1YRtTNP1T2tnI0ju0Qj5jMqYu1I0PCYJSM8X7Itb3595HCs9zENRRZqSpPptZ4uwTnPTxI8Bso6-BTIDAPYDjS804Pj2zMJ3wVJVwjXPatPgUHSascHuExNJ8QJb7_AT9g-GizM-EZUlO73f7-56kwDhNKql6pjYHJT4ExFqiOo3PpA7Eh1Pf9L6qGR5BAgG_SKIEqpdtgFFysn-lSi_Ko-76BD-Jl9vZ_n-IKA4m-mzzUrZlWI-2pi1hN1ZBOtBmS5xUOBcGZNx3Rj6hzsziOQ-_Rjbd5ZbT-7QWfZ7iHRrfNCxqwhP7opwNdjIdrsRZiYgVZibq860wxGpd-PVkIoRb_fVT0Txr9oSXDAA-qKswAk4d_95ImZIBAhzB2b0lvrD9XJROG-WLwqc7mWzR3DdaEJ8DObjgO-8hDRipT7sry_YEFuWneLhDqVclqcybRAFkUUhtyWJoD68LhvMPFpX_vz4zD1eA7MwPbR2dwgK3dkS=w397-h112-no?authuser=0)

  
Reaches the video IDs of the channels using the Youtube Data API service with channel ID information.

#  Technologies

 - [Mysql](https://www.mysql.com/)
 - [Python](https://www.python.org/)
 - [Youtube Data API](https://developers.google.com/youtube/v3)
 - [Requests](https://pypi.org/project/requests/)
 
