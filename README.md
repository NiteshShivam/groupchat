
# Chatting Application




## Role of the Server
Server is receiving all the events from the client and performing the following	action
 - Broadcasting the message
 - sending message to specific client 
 - dealing with the mathematical expression.
## Threads at server side:
    Whenever a new client is added to the server,  a new thread is created.  
    This particular thread deals with that respective client.  
##### As shown in the image:  
    3 users are connected to the server , means 3 threads are running at the server, their id is displayed, along with their name.
![server](https://lh3.googleusercontent.com/pw/AP1GczOlmnwgrdK2ctVt5EuELj8njLVZHNGwWRYI8xdxSTX0ury8-WueSzlHMz_n3xA3DjG6ZmnSG7oHNff-ICchfWIo7KLIHQKQ9jmBmJDvFhyIvhLCA6eG3g-YmSfc4YLTqJguaCkE-SMSThj8Gst6kNUw=w963-h513-s-no-gm?authuser=1)

## Role of client
    As shown 3 clients are connected.  
    At each client ,four functions are given.  
#### Send: 
    it is used for broadcasting the message to all the connected clients.  
#### Calculate:  
    It is used for calculating some mathematical expressions.  
    Here, expressions is written at the client side and calculation  is done at the server side and the result is sent back to the particular client.  
#### Specific user:  
    Instead of broadcasting, if a user wants to chat with a particular user,        then this function will be used.   
    To send the message to specific user need to specify their name along with the message.  
#### Know all users: 
    using this a particular client can know all the connected users.

#### Other functionality:
		When a new user is connected to the server, then a broadcast will happen from  the server telling the name of the new user to the clients.
#### Thread at client side:
		At each client two thread are running,
		First thread is displaying all the messages and dealing with GUI.  
		Second thread is used for receiving the message.

#### Client picture 1: 
    This picture showing when all clients are just connected to the server.
![picture1](https://lh3.googleusercontent.com/pw/AP1GczPAUdEbHeLEGcrfWsZrVLpNygFJ_qn96fNXvXoW_QwNOqkggdduJVeJONDpVWekKf4IdueLHbWO0yBM3irnCXjeqNBg5GPLUrQiweSxAcUJeutrzeqUQnjD6lbOnzn_kheMSfTkKhsz_l4qaAcevFXwZGlMadRPKriMLdvszalqKXlFgly2XhO5djsV76d-puzz7QN8cpziCTOu6sFZvCf-TYV0ZL44IWUX_rddF4QDL22RPvSAgstcs1xA_2lN7oEMxztnt_oDtV6B8lrJy4cMC5WZrWvvtgKFpGzlRI3z3ZwXTHous09zTDAPd661uz9PAkjBCjJ4qrCb7szR1jzPEW56cKQt0uH4Qppj5XleBstQSHLOOqy9ft5tO9atGEYJqjnZ7RamwEBM15jW7BNUYoTzdXtGu6fg-O_tdK9HCrXuyiebzetUfq03R-Nyy25h9gPTxEoCJmK6bNUbuU-1AFpbaxj0CMfrPa_CdS6bNmaWQ18G9-AEUWcpsQ5sqqbw7sKXcUYz6rmrOjMF7Trbw1Hf8_sSziuMsFMb-qSngrxkqws9pNyRpGIQsA1RfnvXjIjFBe4cup5ViArcPD75ajsVKuXP5XNVS7zZYH6n-ing4c-LB0lTQKatCi-JjNnzuqSsCimkOQgrEi_U26AALUxZK-LfjOwE5VkyZ8HfzBVeTRhMFsrtGfzZIT69Oa1jvGptJtBzfKtufNSr2SpD1N5XXtqYFxLNR4fas9szDEy1OAXIcdnT2yf1orOEh8aRZTzaIzY57XNAcWB8Q8ec3QIZDKkf9lcCrNTLrzxYSGEv4loTgr6WeJFpQaxGw3vo3Vz9qKaGk_sEZfakvjf3RS_S0HmRIr4dNcn2hnJqh5jMPFeF0QiUVF4z4aD2hUO_Tv8VXi1JwkEIL8QOhMYGw0CE_nVtTBrTklf4jinujpDCU2MwoBgprLzXvtUlkXvm2JmZ3u40Z9dnO7hqXy5sMLhJSns=w1101-h619-s-no-gm?authuser=1)

#### Client Picture 2: 
    nitesh is using the send button to broadcast the message.

![picture2](https://lh3.googleusercontent.com/pw/AP1GczMSJBEw2vZ31KWSTSDszCUI5gmisOMAOlJeIYcQO6DjRC-zTPv6U5433W8SkORZPGgIYjwYK2a-fbHl8WOj7Lrnk7AijPoZHf4-QZpiIrn0E1LsIrOeRKPqPOTgm6LYscaMyETYnukeBmA-cZySXqL-jrqPUDPbiz16JqvBpKRYVLP_z8xtztxbequVy47VrWexT8-MZ7oab5F2FQ_l4MsuJwE2gslsUlJymK2uD5bGsdSrMDzKFK8lPXB95jLMaKWYo_8lnV3Wm8DFPRBijVSuM3hw457ii6IRVcuUK1cZwGXO0M1IxzUbNmCQQOG7bu664o67vrpUpgXiojnPIEmkCyusiTrWBaB0hJ6ITM362uYpu-yW88YN-d4WsOBIUUzvZiypgzdQUe2u4KqJtVrrjq98rgyT5lJXJ6loW1hHCLZV87VIS8FUnTWZ6XtLzZUcG7WrXV-6ZN0CcHXr-Uo-PQ1QJyjouWScQRFP3sFaNuzuDBDQK8tnaLM2CwkCe4CJ86KYm9_vnIlRtzbBn4wuSyz73GHL4RJ2Y5y3puVhcs07Yb5ekaq3kJiGpcJkDWz-fyFR3HDdHg24KIaNTchCcFZjcAZppeYYWbUq_k4mcRuVOTE5cIveT6kHam80rF-yAdlLIDzkmX9moPATKIdh2Gk2vwnwe3ykpKMM67cQ3RLhPn5gk4rYUc4A0NmwPCYYMSYQwejf936Vc5mDnjtYTkkOHRYbnNqSEUvDTzDw9rKIvR36kE4x5V0WLDBDLy1KUt2vfDyO0eKEjX6sUZSVdL0HaDXcN05mRqs1z691j20TgyyXuDTVrCtXvhnH7hx2BV04gyGr9RzPP9Mg6MmW44AMoURX2b-w0-UVkVsEbnp3Ngf0kCk8MEVeaUCqu_AeP03-ttk5aBNDGqrQsGiuktRoplZz1Djxwl9g3EaLHc2Nyxe97N_H5IiyuYp4Dg8VCyCeTQfgKD6dhdY-dN67lxTNGQ8=w1101-h619-s-no-gm?authuser=1)

#### Client picture 3:
    Hariom has used the calculate function to calculate some expressions and it’s result is display to only hariom.

![picture3](https://lh3.googleusercontent.com/pw/AP1GczO6Cmpz4BPJsre1swx7eGeGdnZf9F7Q2S7fMinNM4RLEMVYZHLtwt09mRQbQArVG4Ks2dBnBYQFju1ZcD9SDb0VT5tn4OTivuJ5HlZ_cIf0C0e_EfKOSZ-7dZ-1samWW6efuyfk38cbacOZ5LUmHJ-bnEc-XnvQZysNsxHKftGk6HNvMnjZhBu0STorHP5aQ0TkkAgZfJZcE4HJFTQiBt4OO3yn_SOq477eCCGrieQ5FTyuDxg_M7ETdYU0Z1067VpqsWQS6tOR4ieS2uRwXPf4eQkAKHgoh565Yy643EcRs6DbYg92gNQRY96cpEa6diBu1ptLOG200KDvEczWj_ixS2-mDaf65VaNq_nJeDd6dCTeG0WW-nqzGlpq-jnzAf5EtP0v7gsd_TRHCJybQjH7uZpoyTF20uzx1iWousaPpJoF1Ehj6ip2M5_6etYPDYM4QJv9ot_ts2b6H8k1TPKPB7QvXo5ZTfsxRzZhZCdNMRhh8g-x0Ne26tsdDPcnGROUBAWJYc_vExHLYtOpjIPiOY9M9qy3oerdqz06i-6ptFo5n8qGjXhW96XeJbAxIgiJrIAp-uMADSzklAlpmJniiJbPoxgJRUXnEP33qHN8Ux1xV_R9dbNniMvPTCqjVCL5Zp7gnQCWs5jXN2Lg7t9fdt4BDFlj47OI71Hlfr8jgMawvU3p4slvKPc6b1AUaIg2aNf2MiHzOpNTDdZ5XpzOB-06SvYoEBrlXg8Rc_kV_M26CHR6szNeWlNBr-jtKpSyYO88hjDg8cL4Tq1GsBjwgH9ZcUKRl7YlcDpjYgkBWUxpE8O19NUAdDNo9CR0KRa4GPTVqqqzYVTDnWWeqbcUWUigL6uFoPOQ9FQ1vSa5zLxMUw3Gq4hAQCj3R5XgfY4YRbHqBKtlFMPdYZvBOiX-cgqw8duqGNmLtmFmIjADw-RbsmnzbdMF6WyDc1KM1t1itPsik55NNJa_98UGI0sL1HMzwLQ=w1101-h619-s-no-gm?authuser=1)


#### Client picture 4:
    Hariom is sending message to only rajat using specific user function.
![picture 5](https://lh3.googleusercontent.com/pw/AP1GczNOdlTH3wohTDh6euZnQkY9uYZfXv-QSXZSHavKbOt6pBqH4T6KIXaiBx5tCAn0nvqq8JXbNbqSXRe6QUsbRPWSHkilN0vFG7C6R8lHkWeuxVXbh9a8Xq1DZ0Zb2K33YoV5pdGclBY64DfbeBaLlcqX2SDqkL_M9l9gdJC4Co2JaSQY0WNNzAWoVSkqZvAPOFHz7j0vdT-9jd2YRT8JRNsXuxKcTAAY2AsbJzsldmBbnPyMnGvqF_878H_lDMFOW_E-k362wReuO_NStpdZmYgaEQNNcEqyoXYdH_uJ0UF0JtfC-y5g0tQmPmQ2gDZGpNqdlARgleiMoartyHamH8oHSGz7aHnaXLAZybb0kRhMmaiFMMgzlyNF_DlhctWjpnxN3Ft0oQOuu-quzDWMD7daQK30j70KBnnkF9LEaToxkP0rjb-8VXRk-AnvqlI3iux9i21BsWKOYAs5KDjW4w5-_2eYy8AfbO9iarsCp3s-h8LCyC9awqx6gnCNSaElXcBa4vLEVnxWJ5PPPiDZnQ-e8NsWUmtVPHTbH7EFKsjrZgfVkn2SSV6xovoSep1ISSBjY9fbSv-1oMpmlSYd9KCtU5fVlhed7P96C258SdDxxgzkouOHwr31VFmlnTYO9Y7nMSSui1jGpqPm2jVAc3c75nhfT-0H58FICb-b8ihr8cXMmrOoEuuyJLMMY-YOugexHXnkUPXwszvoynTkRMmsf_KLlORFxetnQSQwK0zbVCjsLC47JDUg1t-3UAZIxqEhRFKW1slNhpFhGOKTCxIv7-UoKyZoIeoJBCV1MNinqrMTMrSPCq-v8Ntc42p8L0xkm4j7XT8oZ11RYWCSYfV3lv3tmEcct9QYWskCTSqXwsDD2FgRMLzGQbDnJapUU80OZZ2P-WLcdHF4xoyGnQ6GkIfNjtlkq6TW1sgY93CbKLOA1wHSfHb5dGwAjSe1psR0I0PIT3mnMHh8li5SV6QPXrPECCM=w1101-h619-s-no-gm?authuser=1)

#### Client picture 5:
    Hariom has used know all user function to list the all the user connected.
![picture 5](https://lh3.googleusercontent.com/pw/AP1GczPvErNADdREI_uMXxRdEJ5gEGGBIUMv_yYg5uqyEOLcWvSVGO92ZnyXSFEEdWiI_sy6Yto6kucTv1bXRd-LFOwSZmPt9Jipu_9WLs8we1IESxE-axQ4cZ_JugoETDor8CAH-1sZGytsGHs3UwTeEFlTQnFcZ0ywDR5pxNMSJ4BAvCI4VCCIabcAC49faGbUU7tqdz92ecjdvYSu34E4tVMBdDbBsvMhx8f1Gs1SOhqPBD4P3gB3KzJ5oCLPiY7l7nIgsLEqC-q4wBqKoOT4k5-P3qL_pOczNsd4RkmYngmo_k4wf2IfS7p1dS1qmm3ZQzUNVRsP0xE24tQpyW4bGV1oT3RKdlGBmttU-in7u9Rc6ZSZ_AkyrOWDMLhQOtGZ0lHWHTSHbtpJt_j2EY3BPUe9v0IPh9vx3Hv0WsA2-sk9dHaw88gsRqnR7ksaeEoYVNAsDqFl93DaUw24lSOxze5MJj8y8ADwsYd-Nes9FJOoXpoBVkg_ts2xalOCkLy6iGm1hPtZ2lRiv7WbWaaD9iYRmPKOr4OUuWzs5q9b9UZAh_4uwXQyw8EmkFQb6ge79I_CcJoIiQE8pdD6HxfWenmv5xfuV6u-EHJQGWzewE4Za0sH92m5f8nUHm9v0p3U9NWLKdmkZEfGvaiKdNSK-ahOV8XGoM2MogDNCEIkBF81QB2Cw6FirpwYmFMiHMnOFMhFWuvGHRe3YzPQbZ4T2LOuwGTWJL5Y7lkxZnsGOGYN5b5cbiyehtmtKQ0U-XiRbzBh6eV2z9x-k9OttX_It_lPKZHNMN5P1XCWrs8q8c5dlMbrblR93FGdSVfbbNAeVIYilRxHGkEbhViAx0oLHReYJKzOehkXiBr2YhDhqbsrgygH8ANTEGnfD3p9pWAJkvlBCxMrjXvtY-Qo_1hUKdm-AJh7eYYWfeLZS4AWcWB3hy7x_M3N7cg5-YW-VRIeANxFv5fAR9DmDlBrsjkdbids8AuNIys=w1101-h619-s-no-gm?authuser=1)


## Authors

- [@Nitesh](https://www.linkedin.com/in/nitesh-yadav-b8847616b/)


## Deployment

To deploy this project run  
###### First start the server
```bash
  python3 server.py
```
then start the required number of clients

```bash
 python3 client.py
```

## Feedback

If you have any feedback, please reach out to us at     cs23m110@iittp.ac.in   
or niteshyadavand2000nitesh@gmail.com
    

