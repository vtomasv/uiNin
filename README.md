# ✨ Unveiling important nodes in a network  ✨

Written by @nicolas.poza, [@alejandro.alvarez](https://scholar.google.com/citations?user=yzwCzQ4AAAAJ&hl=es), [@tomas.vera](http://vtomasv.net/), @kilvercampos 

The detection of the most important nodes in a graph-database (or network dataset) is a problem of wide interest in various scientific disciplines, particularly in the data sciences. Its relevance has been increasing in recent years thanks to the advances in storage and computing power of modern computers [1]  in the 1990s,  along with the explosive boom in network theory in the early 2000s [2,3,4].

Basically any dataset that can be described through a set of nodes or entities, and a set of links describing how these entities interact or relate between them. Some examples of this type of system (or databases) are:

* Social networks: Where people are represented by nodes, and links represent the different social ties between them (friendship, collaboration, common hobbies, etc.). These kinds of networks appear in technological creations such as Facebook, Twitter, LinkedIn, Instagram, TipTop, etc. In the latter, the most important nodes are related to highly influential people “influencers”, who are of growing interest to modern marketing departments [15]. 

* Biological organisms: The metabolism of an organism can be represented through networks, in which the nodes are biomolecules (metabolites or enzymes) and a metabolite is connected to an enzyme if the former is the educt or product of the enzymatic reaction mediated by the enzyme (metabolomics). We can also relate all the proteins that physically interact in an organism through a protein interaction network (proteomics). The most important nodes are related to possible drug targets, which are of great interest for the design of new treatments, e.g., in parasitic diseases [16]. 

* Transport networks: In this scenario, the nodes represent geographic locations (cities, airports, ports, etc.) and two nodes are connected if there is a route that connects them. For example, in the case of airport networks, two airports are connected if there is a direct flight from one to the other one. The most important nodes are related to the airports through which most people flow if we assume standard commercial flights, and therefore are of great interest to avoid or minimize the spread of pandemics, placing control points and vaccination campaigns at such airports [17]. 

* Computer and IoT devices networks: Here the nodes are composed by all the devices of the IoT ecosystem (smartphones, Arduino-based sensors, raspberry, tablets, smart devices, computers, etc.) and the connections can be wired and/or abstract, e.g., wifi, 3G, 4G, 5G, Bluetooth, etc.

* Seismicity and climate: The versatility of the networks is also shown via the representation of data of temporal nature such as seismicity or climate, which are measured with respect to time. In this case, the nodes are geographical zones and two nodes are connected if there exist correlation or causal relationships [18].

* Online Stores: We can represent the products of an electronic store as a network, in which two products are connected if both were searched or purchased by the same user. Another kind of connection is given by the relationships that these products have (metadata). For example, a tennis racket and socks can share the attributes: sports, outdoors, hobbies, so they could be connected, but not a racket and a bed.

* Internet: In this case, routers are the nodes and the links are wired or wireless connections that allow their communication  [19].

* The WWW (or World Wide Web): allows us to describe the universe of web pages through nodes, and two of these pages are connected if there is a hyperlink from one web page to the other one. Note that in this case, the WWW is a directed network (because it may be a hyperlink from page A to page B, but not necessarily from B to A). We can say that a web page is relevant if a large number of pages "points" to it. The concept of relevance or importance of a web page is used in the design of search engines like google.

All the previous examples allow us to look the data from a different point of view, i.e., as a map of interactions between the elements that compose the system (dataset), and therefore enabling us to take advantage of the existing tools of data mining and artificial intelligence to reveal hierarchies, patterns, vulnerabilities, important elements and so on. It would be extremely difficult from the traditional database schema consisting of a list of records.

### Specifically, what can the analysis of a network offer us?

We will answer this question through an example. Let's imagine that we are trying to create a startup in the world of cargo transport, eg, businesses like FEDEX, DHL, UPS. Minimizing costs is equally important, both for macro-companies and for startups. The first question that we need to ask ourselves is where to place the central warehouse? Although this problem has its origins in a mathematical discipline known as operations research, the new methods offered by network theory allow us to approach to this problem from a new point of view, eg, by the calculation of centrality indexes. In particular, calculating the node (or site) that statistically is closest to any point of the network (closeness centrality index), or through which it is easier to flow from any origin to any destination (betweenness centrality index). This is one of the thousands of examples where finding the most central node is valuable for a company.

_"In the following paper, we will be interested in detecting the most important, relevant, influential or central nodes."_

Depending on the system under study, the concept of importance, relevance or influence may vary, however, for most systems, the most important node is the 

* Most connected (degree centrality [5]).
* The closest to the rest of the nodes on average (closeness centrality [6]). 
* Through which passes more information (betweenness centrality [7]).
* The connection to other important nodes (eigenvector centrality [8]).
* Among many others [9].

Here we will be interested in methods based on information flow. 
Typically observing a taxi driver does not go from point A to point B by the shortest route because the shortest path between two points in the road network of a city suffers from the bottleneck effect (e.g. is saturated). Instead, the taxi driver travels by other routes that end up being more efficient than the shortest route. The same occurs in the informational context, the information does not always travel by the shortest path. Then, the classical intermediation measure does not exploit all the information offered by the diversity of paths that exist between two points in a network.
Inspired by Mark Newman's paper [13], in the following we explore his methodology from a simpler approach, that is, modelling the flow of an information packet in a network through an absorbent uniform random walk. We will refer to this method hereinafter as the Newman method.


### References

1. Grochowski, EG, Hoyt, RF & Heath, JS Magnetic Hard Disk Drive Form Factor Evolution. IEEE Transactions on Magnetics 29, 4065–4067 (1993).
2. A. Barabasi, E. Bonabeau (2003). "Scale-Free Networks". Scientific American: 50–59.
3. SH Strogatz, DJ Watts (1998). "Collective dynamics of 'small-world' networks". Nature. 393 (6684): 440–442.
4. Amaral, LAN, Scala, A., Barthélémy, M. & Stanley, HE Classes of small-world networks. in Proceedings of the National Academy of Sciences of the United States of America 97, 11149–11152 (2000).
5. Wasserman, S. & Faust, K Social Network Analysis Methods and Applications. (Cambridge University Press, 1944).
6. Sabidussi, G. The centrality index of a graph. Psychometrika. 31, 4, 581-603 (1996).
7. Brandes, U. A faster algorithm for betweenness centrality. The Jour. Math. Partner. 25, 163-177 (2001).
8. Bonacich, P. Power and Centrality: A family of measures. Am. Jour. Soc. 92, 1170 (1987).
9. Lü, L. et al. Vital nodes identification in complex networks. Physics Reports 650, 1–63 (2016) .650, 
10. Padgett, JF & Ansell, CK Robust action and the rise of the Medici, 1400–1434. Am. Jour. Soc. 98, 1259 (1993).
11. Matthew, J. Social and Economic Networks. (Princeton University Press, 2010).
12. Zachary WW An information flow model for conflict and fission in small groups. Jour. Anth. Res. 33,452-473 (1977).
13. Newman, MEJ (2005). "A measure of betweenness centrality based on random walks". Social Networks 27: 39-54.
14. Knuth DE The Stanford GraphBase: A Platform for Combinatorial Computing. (Addison-Wesley, Reading, MA, 1993).
15. [https://medium.com/swlh/what-is-influencer-marketing-the-complete-guide-2ef95a6eb4a3](https://medium.com/swlh/what-is-influencer-marketing-the-complete-guide-2ef95a6eb4a3)
16. Herrera-Almarza G., et al. Properties of essential genes in the protein-protein interaction network of Escherichia coli from the perspective of network theory, Journal of Computational Methods in Sciences and Engineering 17 (1), 209-216 (2017).
17. Pastor-Satorras, R., Castellano, C., Van Mieghem, P. & Vespignani, A. Epidemic processes in complex networks. Reviews of Modern Physics 87, (2015).
18. Yook, SH, Jeong, H. & Barabási, AL Modeling the internet's large-scale topology. Proceedings of the National Academy of Sciences of the United States of America 99, 13382-13386 (2002).
19. Bottinelli, A., Perna, A., Ward, A. & Sumpter, D. Proceedings of the European Conference on Complex Systems 2012. in Proceedings of the European Conference on Complex Systems 2012591–606 (2013). doi: 10.1007 / 978-3-319-00395-5
