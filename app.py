#!/usr/bin/env python
##########################################################################
# code app.py the application for HCSD (Human Cancer Secretome Database). 
#
# Author: Amir Feizi
# Date:   April 05, 2015
# Email: feizi@chalmers.se
#
# Copyright (c) 2014, 2017 www.cancersecretome.org
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#   - Redistributions of source code must retain the above
#     copyright notice, this list of conditions and the
#     following disclaimer.
#   - Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer
#     in the documentation and/or other materials provided with the
#     distribution.
#   - Neither the name of the author nor the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#########################################################################
import web
import os
import sys
import StringIO
import math


urls = (
  '/','Home','/home','Home','/study','Study','/search','Search','/result1','Index','/result3','Result3','/empty','Empty','/result2','Result2','/download1','Download','/download2','Download2','/results4','Results4','/contact','Contact','/help','Help','/data','Data'
,'/test','Test','/download4','Download4','/news','News','/feed','Feed')

app = web.application(urls, globals())
render1 = web.template.render('templates/', base="layout1")
render2=web.template.render('templates/')
render3 = web.template.render('templates/',base="layout2")
render4=web.template.render('templates/',base="layout3")

global gene,seq,ref,sub,des,fun,sub,sim,psim1


class Index(object):
	
	
	def POST(self):
		form1=web.input	(bx01="a")
		form2=web.input	(bx02="b")
		form3=web.input	(bx03="c")
		form4=web.input (bx04="d")		

		if form1.bx01 and form2.bx02 and form3.bx03 :
			if form2.bx02=="all_types":
				if form3.bx03=="l_free":

					db = web.database(dbn = 'mysql', db = 'HCSD', user = 'root', pw= 'istanbul')
					entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
					
					if not entries:
						a1="No result has found"
						return render1.empty(a1=a1)	
					else:
						
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a1=entries[0]
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a2=entries[0].Gene_ID
						a2_1="http://www.ncbi.nlm.nih.gov/sites/entrez?db=gene&amp;cmd=Retrieve&amp;dopt=Graphics&amp;list_uids="+a2
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a3=entries[0].Ensembl_Gene_ID
						a3_1="http://sep2013.archive.ensembl.org/Homo_sapiens/geneview?gene="+a3
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a4=entries[0].UniProt_Accession
						a4_1="http://www.uniprot.org/entry/"+a4
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a26=entries[0].Sequence.replace(" ","")
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})[0]			
						a11=entries.PTM
						a11=a11.split(" ")
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})[0]			
						a12=entries.secondary_info
						a12=a12.split(" ")
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})[0]			
						a13=entries.Sequence
						a14=[]
						a15=[]
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id",vars={'id':form1.bx01})
						ensembl=entries[0].Ensembl_Gene_ID
						a16=db.query("SELECT * FROM D3 WHERE Ensembl_Gene_ID=$id ", vars={'id':ensembl})
						
	
						for j in a12:
								if j=="2":
									a14.append(1)

								elif j=="1":
									a14.append(2)
								elif j=="3":
									a14.append(3)
								elif j=="4":
									a14.append(4)
								elif j=="5":
									a14.append(5)
								elif j=="0":
									a14.append(0)

										
						for k in a11:
							if k=="6":
								a15.append(7)
							elif k=="7":
								a15.append(8)
							elif k=="8":
								a15.append(9)
							
							elif k=="0":
								a15.append(0)

					

						return render1.download1(a1=a1,a2=a2,a2_1=a2_1,a3=a3,a3_1=a3_1,a4=a4,a4_1=a4_1,a14=a14,a15=a15,a26=a26,a16=a16)
						#return render1.test(a0=a0)				
			



				if form3.bx03=="l_based":

					db = web.database(dbn = 'mysql', db = 'HCSD', user = 'root', pw= 'istanbul')
					entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
					
					if not entries:
						a1="No result has found"
						return render1.empty(a1=a1)	
									
					else:
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a1=entries[0]
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a2=entries[0].Gene_ID
						a2_1="http://www.ncbi.nlm.nih.gov/sites/entrez?db=gene&amp;cmd=Retrieve&amp;dopt=Graphics&amp;list_uids="+a2
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a3=entries[0].Ensembl_Gene_ID
						a3_1="http://sep2013.archive.ensembl.org/Homo_sapiens/geneview?gene="+a3
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a4=entries[0].UniProt_Accession
						a4_1="http://www.uniprot.org/entry/"+a4
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a26=entries[0].Sequence.replace(" ","")
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})[0]			
						a11=entries.PTM
						a11=a11.split(" ")
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})[0]			
						a12=entries.secondary_info
						a12=a12.split(" ")
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})[0]			
						a13=entries.Sequence
						a14=[]
						a15=[]
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id",vars={'id':form1.bx01})
						gene_symbol=entries[0].Gene_symbol
						a17=db.query("SELECT * FROM D11 WHERE   gene_symbol=$id1 ",vars={'id1':gene_symbol})
						a18=db.query("SELECT * FROM D11 WHERE  gene_symbol=$id1 ",vars={'id1':gene_symbol})
						
						a20=db.query("SELECT * FROM D11 WHERE  gene_symbol=$id1 ",vars={'id1':gene_symbol})
						a21=db.query("SELECT * FROM D11 WHERE gene_symbol=$id1 ",vars={'id1':gene_symbol})
						a22=db.query("SELECT * FROM D11 WHERE  gene_symbol=$id1 ",vars={'id1':gene_symbol})
						a23=db.query("SELECT * FROM D11 WHERE gene_symbol=$id1 ",vars={'id1':gene_symbol})
						a24=db.query("SELECT * FROM D11 WHERE  gene_symbol=$id1 ",vars={'id1':gene_symbol})
						a27=db.query("SELECT * FROM D11 WHERE  gene_symbol=$id1 ",vars={'id1':gene_symbol})
						a28=db.query("SELECT * FROM D11 WHERE  gene_symbol=$id1 ",vars={'id1':gene_symbol})

 						a29=db.query("SELECT * FROM D11 WHERE  gene_symbol=$id1 ",vars={'id1':gene_symbol})
						
						a25=len(a24)
						a19=[]
						for i in range(a25):
							#a6=db.query("SELECT min(fold_change) as fold_change FROM D11")[0].fold_change
							#a7=db.query("SELECT max(fold_change) as fold_change FROM D11")[0].fold_change
							a8=db.query("SELECT * FROM D11 WHERE Gene_symbol=$id1",vars={'id1':gene_symbol})
							a9=a8[i].fold_change
							#a9=(math.floor((a9-a6)/(a7-a6)*100))
							#a19.append(str(a9)+"px")
							if a9>0:
							   a19.append("up")
							if a9==0:
							   a19.append("flat")
							if a9<0:
							   a19.append("down")
				
						for j in a12:
								if j=="2":
									a14.append(1)

								elif j=="1":
									a14.append(2)
								elif j=="3":
									a14.append(3)
								elif j=="4":
									a14.append(4)
								elif j=="5":
									a14.append(5)
								elif j=="0":
									a14.append(0)

										
						for k in a11:
							if k=="6":
								a15.append(7)
							elif k=="7":
								a15.append(8)
							elif k=="8":
								a15.append(9)
							
							elif k=="0":
								a15.append(0)

						
						
						return render1.download3(a1=a1,a2=a2,a2_1=a2_1,a3=a3,a3_1=a3_1,a4=a4,a4_1=a4_1,a14=a14,a15=a15,a26=a26,a17=a17,a18=a18,a19=a19,a20=a20,a21=a21,a22=a22,a23=a23,a27=a27,a28=a28,a29=a29)		

	




				if form3.bx03=="both":	
					db = web.database(dbn = 'mysql', db = 'HCSD', user = 'root', pw= 'istanbul')
					entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
					if not entries:
						a1="No result has found"
						return render1.empty(a1=a1)	
					else:
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a1=entries[0]
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a2=entries[0].Gene_ID
						a2_1="http://www.ncbi.nlm.nih.gov/sites/entrez?db=gene&amp;cmd=Retrieve&amp;dopt=Graphics&amp;list_uids="+a2
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a3=entries[0].Ensembl_Gene_ID
						a3_1="http://sep2013.archive.ensembl.org/Homo_sapiens/geneview?gene="+a3
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a4=entries[0].UniProt_Accession
						a4_1="http://www.uniprot.org/entry/"+a4
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a26=entries[0].Sequence.replace(" ","")
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})[0]			
						a11=entries.PTM
						a11=a11.split(" ")
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})[0]			
						a12=entries.secondary_info
						a12=a12.split(" ")
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})[0]			
						a13=entries.Sequence
						a14=[]
						a15=[]
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id",vars={'id':form1.bx01})
						ensembl=entries[0].Ensembl_Gene_ID
						a16=db.query("SELECT * FROM D3 WHERE Ensembl_Gene_ID=$id ", vars={'id':ensembl})
						a17=db.query("SELECT * FROM D12 WHERE   Ensembl_Gene_ID=$id1 ",vars={'id1':ensembl})
						a18=db.query("SELECT * FROM D12 WHERE  Ensembl_Gene_ID=$id1 ",vars={'id1':ensembl})
						a20=db.query("SELECT * FROM D12 WHERE  Ensembl_Gene_ID=$id1 ",vars={'id1':ensembl})
						a21=db.query("SELECT * FROM D12 WHERE   Ensembl_Gene_ID=$id1 ",vars={'id1':ensembl})
						a22=db.query("SELECT * FROM D12 WHERE  Ensembl_Gene_ID=$id1 ",vars={'id1':ensembl})
						a23=db.query("SELECT * FROM D12 WHERE  Ensembl_Gene_ID=$id1 ",vars={'id1':ensembl})
						a24=db.query("SELECT * FROM D12 WHERE  Ensembl_Gene_ID=$id1 ",vars={'id1':ensembl})
						a27=db.query("SELECT * FROM D12 WHERE  Ensembl_Gene_ID=$id1 ",vars={'id1':ensembl})
						a25=len(a24)
						a19=[]
						for i in range(a25):
							#a6=db.query("SELECT min(Fold_change) as Fold_change FROM D2")[0].Fold_change
							#a7=db.query("SELECT max(Fold_change) as Fold_change FROM D2")[0].Fold_change
							a8=db.query("SELECT * FROM D2 WHERE Ensembl_Gene_ID=$id1",vars={'id1':ensembl})
							a9=a8[i].Fold_change
							#a9=(math.floor((a9-a6)/(a7-a6)*100))
							#a19.append(str(a9)+"px")
				
							if a9>0:
                                                           a19.append("up")
                                                        if a9==0:
                                                           a19.append("flat")
                                                        if a9<0:
                                                           a19.append("down")

						for j in a12:
								if j=="2":
									a14.append(1)

								elif j=="1":
									a14.append(2)
								elif j=="3":
									a14.append(3)
								elif j=="4":
									a14.append(4)
								elif j=="5":
									a14.append(5)
								elif j=="0":
									a14.append(0)

										
						for k in a11:
							if k=="6":
								a15.append(7)
							elif k=="7":
								a15.append(8)
							elif k=="8":
								a15.append(9)
							
							elif k=="0":
								a15.append(0)

						
						
						return render1.download2(a1=a1,a2=a2,a2_1=a2_1,a3=a3,a3_1=a3_1,a4=a4,a4_1=a4_1,a14=a14,a15=a15,a26=a26,a16=a16,a17=a17,a18=a18,a19=a19,a20=a20,a21=a21,a22=a22,a23=a23,a27=a27)		



			elif form2.bx02!="all_types":
			
				if form3.bx03=="l_free":				
					db = web.database(dbn = 'mysql', db = 'HCSD', user = 'root', pw= 'istanbul')
					a1=db.query("SELECT * FROM D3 WHERE Gene_symbol=$id1  ",vars={'id1':form1.bx01})
					if not a1:
						a1="No result has found"
						return render1.empty(a1=a1)	
					else:
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a1=entries[0]
						entries=db.query("SELECT Gene_symbol,Gene_ID,Ensembl_Gene_ID,UniProt_Accession,Transcript_count,Gene_Start_bp,Gene_End_bp,Chromosome_Name,Description,No_of_cancer_type_identified,$id2,SignalP4_D,SecretomeP5,TMHMM6,Detected_in_the_HPPP,Sequence,Function,Gene_ontology_GO,Synonymous,PMID FROM D3 WHERE Gene_symbol=$id1  ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a2=entries[0].Gene_ID
						a2_1="http://www.ncbi.nlm.nih.gov/sites/entrez?db=gene&amp;cmd=Retrieve&amp;dopt=Graphics&amp;list_uids="+a2
						entries=db.query("SELECT Gene_symbol,Gene_ID,Ensembl_Gene_ID,UniProt_Accession,Transcript_count,Gene_Start_bp,Gene_End_bp,Chromosome_Name,Description,No_of_cancer_type_identified,$id2,SignalP4_D,SecretomeP5,TMHMM6,Detected_in_the_HPPP,Sequence,Function,Gene_ontology_GO,Synonymous,PMID FROM D3 WHERE Gene_symbol=$id1  ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a3=entries[0].Ensembl_Gene_ID
						a3_1="http://sep2013.archive.ensembl.org/Homo_sapiens/geneview?gene="+a3
						entries=db.query("SELECT Gene_symbol,Gene_ID,Ensembl_Gene_ID,UniProt_Accession,Transcript_count,Gene_Start_bp,Gene_End_bp,Chromosome_Name,Description,No_of_cancer_type_identified,$id2,SignalP4_D,SecretomeP5,TMHMM6,Detected_in_the_HPPP,Sequence,Function,Gene_ontology_GO,Synonymous,PMID FROM D3 WHERE Gene_symbol=$id1  ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a4=entries[0].UniProt_Accession
						a4_1="http://www.uniprot.org/entry/"+a4
						a5=form2.bx02
						a7=db.query("SELECT * FROM D3 WHERE Gene_symbol=$id1 ",vars={'id1':form1.bx01})
						entries=db.query("SELECT * FROM D3 WHERE Gene_symbol=$id", vars={'id':form1.bx01})
						a26=entries[0].Sequence.replace(" ","")
						entries=db.query("SELECT * FROM D3 WHERE Gene_symbol=$id", vars={'id':form1.bx01})[0]			
						a11=entries.PTM
						a11=a11.split(" ")[:-1]
						entries=db.query("SELECT * FROM D3 WHERE Gene_symbol=$id", vars={'id':form1.bx01})[0]			
						a12=entries.secondary_info
						a12=a12.split(" ")[:-1]
						entries=db.query("SELECT * FROM D3 WHERE Gene_symbol=$id", vars={'id':form1.bx01})[0]			
						a13=entries.Sequence
						a14=[]
						a15=[]

						
		
						for j in a12:
								if j=="2":
									a14.append(1)

								elif j=="1":
									a14.append(2)
								elif j=="3":
									a14.append(3)
								elif j=="4":
									a14.append(4)
								elif j=="5":
									a14.append(5)
								elif j=="0":
									a14.append(0)

										
						for k in a11:
							if k=="6":
								a15.append(7)
							elif k=="7":
								a15.append(8)
							elif k=="8":
								a15.append(9)
							
							elif k=="0":
								a15.append(0)	
					
		
						a6=db.query("SELECT Gene_symbol,Gene_ID,Ensembl_Gene_ID,UniProt_Accession,Transcript_count,Gene_Start_bp,Gene_End_bp,Chromosome_Name,Description,No_of_cancer_type_identified,$id2,SignalP4_D,SecretomeP5,TMHMM6,Subcellular_location,Detected_in_the_HPPP,Sequence,Function,Gene_ontology_GO,Synonymous,PMID FROM D3 WHERE Gene_symbol=$id1  ",vars={'id1':form1.bx01,'id2':form3.bx03})[0]

						
						return render1.result2(a1=a1,a2_1=a2_1,a3=a3,a3_1=a3_1,a4=a4,a4_1=a4_1,a5=a5,a6=a6,a7=a7,a26=a26,a14=a14,a15=a15)
			
				elif form3.bx03=="l_based":
				
					db = web.database(dbn = 'mysql', db = 'HCSD', user = 'root', pw= 'istanbul')	
					a1=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
					if not a1:
						a1="No result has found"
						return render1.empty(a1=a1)	
					else:		
						
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a1=entries[0]
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a2=entries[0].Gene_ID
						a2_1="http://www.ncbi.nlm.nih.gov/sites/entrez?db=gene&amp;cmd=Retrieve&amp;dopt=Graphics&amp;list_uids="+a2
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a3=entries[0].Ensembl_Gene_ID
						a3_1="http://sep2013.archive.ensembl.org/Homo_sapiens/geneview?gene="+a3
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a4=entries[0].UniProt_Accession
						a4_1="http://www.uniprot.org/entry/"+a4
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a26=entries[0].Sequence.replace(" ","")
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})[0]			
						a18=entries.PTM
						a18=a18.split(" ")[:-1]
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})[0]			
						a19=entries.secondary_info
						a19=a19.split(" ")[:-1]
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})[0]			
						a20=entries.Sequence
										

						a5=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a14=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a15=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a16=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a17=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						
						a28=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a29=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a24=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a30=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a31=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})


						a21=[]
						a22=[]
						
						
						for j in a19:
								if j=="2":#red helix
									a21.append(1)

								elif j=="1":#green TM
									a21.append(2)
								elif j=="3":# blue strand
									a21.append(3)
								elif j=="4":#greay turn
									a21.append(4)
								elif j=="5": #yello signal peptide
									a21.append(5)
								else:
									a21.append(0)

										
						for k in a18:
							if k=="6":#yellow disulfide
								a22.append(7)
						
							if k=="7":#brown n-linked pot
								a22.append(8)
						
							if k=="8":#brown o-linked
								a22.append(9)
						
							else:
								a22.append(0)	
						
						a25=len(a24)
						a10=[]
						for i in range(a25):
							a6=db.query("SELECT min(fold_change) as fold_change FROM D11")[0].fold_change
							a7=db.query("SELECT max(Fold_change) as fold_change FROM D11")[0].fold_change
							a8=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
							a9=a8[i].fold_change
							a9=(math.floor((a9-a6)/(a7-a6)*100))
							a10.append(str(a9)+"px")

						return render1.result3(a1=a1,a2_1=a2_1,a3_1=a3_1,a4_1=a4_1,a5=a5,a10=a10,a14=a14,a15=a15,a16=a16,a17=a17,a18=a18,a19=a19,a21=a21,a22=a22,a26=a26,a28=a28,a29=a29,a30=a30,a31=a31)

	
				elif form3.bx03=="both":	
					db = web.database(dbn = 'mysql', db = 'HCSD', user = 'root', pw= 'istanbul')
					entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
					if not entries:
						a1="No result has found"
						return render1.empty(a1=a1)	
					else:
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a1=entries[0]
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a2=entries[0].Gene_ID
						a2_1="http://www.ncbi.nlm.nih.gov/sites/entrez?db=gene&amp;cmd=Retrieve&amp;dopt=Graphics&amp;list_uids="+a2
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a3=entries[0].Ensembl_Gene_ID
						a3_1="http://sep2013.archive.ensembl.org/Homo_sapiens/geneview?gene="+a3
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a4=entries[0].UniProt_Accession
						a4_1="http://www.uniprot.org/entry/"+a4
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})
						a7=db.query("SELECT * FROM D3 WHERE Gene_symbol=$id1 ",vars={'id1':form1.bx01})
						if len(a7)==0:
							a7="not"
						a26=entries[0].Sequence.replace(" ","")
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})[0]			
						a11=entries.PTM
						a11=a11.split(" ")
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})[0]			
						a12=entries.secondary_info
						a12=a12.split(" ")
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id", vars={'id':form1.bx01})[0]			
						a5=form2.bx02

						a13=entries.Sequence
						a14=[]
						a15=[]
						entries=db.query("SELECT * FROM D6 WHERE Gene_symbol=$id OR  Ensembl_Gene_ID=$id OR UniProt_Accession=$id",vars={'id':form1.bx01})
						gene_symbol=entries[0].Gene_symbol
						a28=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						if len(a28)==0:
							a28="not"
						a16=db.query("SELECT * FROM D3 WHERE Gene_symbol=$id ", vars={'id':gene_symbol})
	
						a17=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a18=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a20=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a21=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a22=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a23=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a24=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a27=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a29=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})
						a30=db.query("SELECT * FROM D11 WHERE D11.cancer_type LIKE $id2 and Gene_symbol=$id1 ",vars={'id1':form1.bx01,'id2':form2.bx02})

						a25=len(a24)
						a19=[]
						for i in range(a25):
						#	a6=db.query("SELECT min(fold_change) as fold_change FROM D11")[0].fold_change
						#	a7=db.query("SELECT max(fold_change) as fold_change FROM D11")[0].fold_change
							a8=db.query("SELECT * FROM D11 WHERE gene_symbol=$id1",vars={'id1':gene_symbol})
							a9=a8[i].fold_change
						#	a9=(math.floor((a9-a6)/(a7-a6)*100))
						#	a19.append(str(a9)+"px")
		
							if a9>0:
                                                           a19.append("up")
                                                        if a9==0:
                                                           a19.append("flat")
                                                        if a9<0:
                                                           a19.append("down")

						for j in a12:
								if j=="2":
									a14.append(1)

								elif j=="1":
									a14.append(2)
								elif j=="3":
									a14.append(3)
								elif j=="4":
									a14.append(4)
								elif j=="5":
									a14.append(5)
								elif j=="0":
									a14.append(0)

										
						for k in a11:
							if k=="6":
								a15.append(7)
							elif k=="7":
								a15.append(8)
							elif k=="8":
								a15.append(9)
							
							elif k=="0":
								a15.append(0)

						
						
						return render1.download4(a1=a1,a2=a2,a2_1=a2_1,a3=a3,a3_1=a3_1,a4=a4,a4_1=a4_1,a5=a5,a7=a7,a14=a14,a15=a15,a26=a26,a16=a16,a17=a17,a18=a18,a19=a19,a20=a20,a21=a21,a22=a22,a23=a23,a27=a27,a28=a28,a29=a29,a30=a30)		



			
class Home(object):

    def GET(self):


       return render2.home()
    def POST(self):
                
                form1=web.input	(bx01="a")

		
		if form1.bx01:
			db = web.database(dbn = 'mysql', db = 'HCSD', user = 'root',pw= 'istanbul', host='mysql.server')
							
		return render1.Index(db=db)



class Contact(object):

    def GET(self):


       return render2.contact()


class News(object):

    def GET(self):


       return render2.news()


class Help(object):

    def GET(self):


       return render3.help()


class Data(object):

    def GET(self):


       return render2.data()


class Search(object):

    def GET(self):


       return render2.search()

class Download(object):

    def GET(self):


       return render1.download()


class Study(object):
	def GET(self):
		form=web.input(pubmed=None)
		db = web.database(dbn = 'mysql', db = 'HCSD', user = 'root', pw= 'istanbul')
		a1=str(form.pubmed)
		a2=db.query("SELECT * FROM D10 WHERE D10.pubmed LIKE $id1",vars={'id1':a1})[0]
		a2_1=a2.study.split(">")
		a3=a2_1[0]
		a4=a2_1[1]
			
		
		return render4.study(a2=a2,a3=a3,a4=a4)

class Download2(object):

    def GET(self):
       return render1.download2()
class Download4(object):

    def GET(self):
       return render1.download4()


class Test(object):

    def GET(self):


       return render1.test()

		
class Result2(object):
	def GET(self):
		return render1.result2()
class Empty(object):
	def GET(self):
		return render1.empty()


class Feed(object):
	def POST(self):
		i= web.input()
		db = web.database(dbn = 'mysql', db = 'HCSD', user = 'root', pw= 'istanbul')
        	n=db.insert('feed', name=i.name,email=i.email,message=i.message,selection=i.selection)
		raise web.seeother('/')

		
if __name__ == "__main__":
    app.run()


