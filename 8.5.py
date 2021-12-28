#The double split pattern

fh = """From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.90])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Sat, 05 Jan 2008 09:14:16 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Sat, 05 Jan 2008 09:14:16 -0500
Received: from holes.mr.itd.umich.edu (holes.mr.itd.umich.edu [141.211.14.79])
	by flawless.mail.umich.edu () with ESMTP id m05EEFR1013674;
	Sat, 5 Jan 2008 09:14:15 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY holes.mr.itd.umich.edu ID 477F90B0.2DB2F.12494 ; 
	 5 Jan 2008 09:14:10 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 5F919BC2F2;
	Sat,  5 Jan 2008 14:10:05 +0000 (GMT)
Message-ID: <200801051412.m05ECIaH010327@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 899
          for <source@collab.sakaiproject.org>;
          Sat, 5 Jan 2008 14:09:50 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id A215243002
	for <source@collab.sakaiproject.org>; Sat,  5 Jan 2008 14:13:33 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m05ECJVp010329
	for <source@collab.sakaiproject.org>; Sat, 5 Jan 2008 09:12:19 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m05ECIaH010327
	for source@collab.sakaiproject.org; Sat, 5 Jan 2008 09:12:18 -0500
Date: Sat, 5 Jan 2008 09:12:18 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
To: source@collab.sakaiproject.org
From: stephen.marquard@uct.ac.za
Subject: [sakai] svn commit: r39772 - content/branches/sakai_2-5-x/content-impl/impl/src/java/org/sakaiproject/content/impl
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Sat Jan  5 09:14:16 2008
X-DSPAM-Confidence: 0.8475
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39772

Author: stephen.marquard@uct.ac.za
Date: 2008-01-05 09:12:07 -0500 (Sat, 05 Jan 2008)
New Revision: 39772

Modified:
content/branches/sakai_2-5-x/content-impl/impl/src/java/org/sakaiproject/content/impl/ContentServiceSqlOracle.java
content/branches/sakai_2-5-x/content-impl/impl/src/java/org/sakaiproject/content/impl/DbContentService.java
Log:
SAK-12501 merge to 2-5-x: r39622, r39624:5, r39632:3 (resolve conflict from differing linebreaks for r39622)

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.97])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 18:10:48 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 18:10:48 -0500
Received: from icestorm.mr.itd.umich.edu (icestorm.mr.itd.umich.edu [141.211.93.149])
	by sleepers.mail.umich.edu () with ESMTP id m04NAbGa029441;
	Fri, 4 Jan 2008 18:10:37 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY icestorm.mr.itd.umich.edu ID 477EBCE3.161BB.4320 ; 
	 4 Jan 2008 18:10:31 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 07969BB706;
	Fri,  4 Jan 2008 23:10:33 +0000 (GMT)
Message-ID: <200801042308.m04N8v6O008125@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 710
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 23:10:10 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 4BA2F42F57
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 23:10:10 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m04N8vHG008127
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 18:08:57 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m04N8v6O008125
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 18:08:57 -0500
Date: Fri, 4 Jan 2008 18:08:57 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to louis@media.berkeley.edu using -f
To: source@collab.sakaiproject.org
From: louis@media.berkeley.edu
Subject: [sakai] svn commit: r39771 - in bspace/site-manage/sakai_2-4-x/site-manage-tool/tool/src: bundle java/org/sakaiproject/site/tool
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 18:10:48 2008
X-DSPAM-Confidence: 0.6178
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39771

Author: louis@media.berkeley.edu
Date: 2008-01-04 18:08:50 -0500 (Fri, 04 Jan 2008)
New Revision: 39771

Modified:
bspace/site-manage/sakai_2-4-x/site-manage-tool/tool/src/bundle/sitesetupgeneric.properties
bspace/site-manage/sakai_2-4-x/site-manage-tool/tool/src/java/org/sakaiproject/site/tool/SiteAction.java
Log:
BSP-1415 New (Guest) user Notification

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From zqian@umich.edu Fri Jan  4 16:10:39 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.25])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 16:10:39 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 16:10:39 -0500
Received: from ghostbusters.mr.itd.umich.edu (ghostbusters.mr.itd.umich.edu [141.211.93.144])
	by panther.mail.umich.edu () with ESMTP id m04LAcZw014275;
	Fri, 4 Jan 2008 16:10:38 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY ghostbusters.mr.itd.umich.edu ID 477EA0C6.A0214.25480 ; 
	 4 Jan 2008 16:10:33 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id C48CDBB490;
	Fri,  4 Jan 2008 21:10:31 +0000 (GMT)
Message-ID: <200801042109.m04L92hb007923@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 906
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 21:10:18 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 7D13042F71
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 21:10:14 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m04L927E007925
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 16:09:02 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m04L92hb007923
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 16:09:02 -0500
Date: Fri, 4 Jan 2008 16:09:02 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to zqian@umich.edu using -f
To: source@collab.sakaiproject.org
From: zqian@umich.edu
Subject: [sakai] svn commit: r39770 - site-manage/branches/sakai_2-5-x/site-manage-tool/tool/src/webapp/vm/sitesetup
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 16:10:39 2008
X-DSPAM-Confidence: 0.6961
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39770

Author: zqian@umich.edu
Date: 2008-01-04 16:09:01 -0500 (Fri, 04 Jan 2008)
New Revision: 39770

Modified:
site-manage/branches/sakai_2-5-x/site-manage-tool/tool/src/webapp/vm/sitesetup/chef_site-siteInfo-list.vm
Log:
merge fix to SAK-9996 into 2-5-x branch: svn merge -r 39687:39688 https://source.sakaiproject.org/svn/site-manage/trunk/

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From rjlowe@iupui.edu Fri Jan  4 15:46:24 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.25])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 15:46:24 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 15:46:24 -0500
Received: from dreamcatcher.mr.itd.umich.edu (dreamcatcher.mr.itd.umich.edu [141.211.14.43])
	by panther.mail.umich.edu () with ESMTP id m04KkNbx032077;
	Fri, 4 Jan 2008 15:46:23 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY dreamcatcher.mr.itd.umich.edu ID 477E9B13.2F3BC.22965 ; 
	 4 Jan 2008 15:46:13 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 4AE03BB552;
	Fri,  4 Jan 2008 20:46:13 +0000 (GMT)
Message-ID: <200801042044.m04Kiem3007881@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 38
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 20:45:56 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id A55D242F57
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 20:45:52 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m04KieqE007883
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 15:44:40 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m04Kiem3007881
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 15:44:40 -0500
Date: Fri, 4 Jan 2008 15:44:40 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to rjlowe@iupui.edu using -f
To: source@collab.sakaiproject.org
From: rjlowe@iupui.edu
Subject: [sakai] svn commit: r39769 - in gradebook/trunk/app/ui/src: java/org/sakaiproject/tool/gradebook/ui/helpers/beans java/org/sakaiproject/tool/gradebook/ui/helpers/producers webapp/WEB-INF webapp/WEB-INF/bundle
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 15:46:24 2008
X-DSPAM-Confidence: 0.7565
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39769

Author: rjlowe@iupui.edu
Date: 2008-01-04 15:44:39 -0500 (Fri, 04 Jan 2008)
New Revision: 39769

Modified:
gradebook/trunk/app/ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/beans/AssignmentGradeRecordBean.java
gradebook/trunk/app/ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/producers/GradeGradebookItemProducer.java
gradebook/trunk/app/ui/src/webapp/WEB-INF/applicationContext.xml
gradebook/trunk/app/ui/src/webapp/WEB-INF/bundle/messages.properties
gradebook/trunk/app/ui/src/webapp/WEB-INF/requestContext.xml
Log:
SAK-12180 - Fixed errors with grading helper

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From zqian@umich.edu Fri Jan  4 15:03:18 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.46])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 15:03:18 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 15:03:18 -0500
Received: from firestarter.mr.itd.umich.edu (firestarter.mr.itd.umich.edu [141.211.14.83])
	by fan.mail.umich.edu () with ESMTP id m04K3HGF006563;
	Fri, 4 Jan 2008 15:03:17 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY firestarter.mr.itd.umich.edu ID 477E9100.8F7F4.1590 ; 
	 4 Jan 2008 15:03:15 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 57770BB477;
	Fri,  4 Jan 2008 20:03:09 +0000 (GMT)
Message-ID: <200801042001.m04K1cO0007738@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 622
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 20:02:46 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id AB4D042F4D
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 20:02:50 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m04K1cXv007740
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 15:01:38 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m04K1cO0007738
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 15:01:38 -0500
Date: Fri, 4 Jan 2008 15:01:38 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to zqian@umich.edu using -f
To: source@collab.sakaiproject.org
From: zqian@umich.edu
Subject: [sakai] svn commit: r39766 - site-manage/branches/sakai_2-4-x/site-manage-tool/tool/src/java/org/sakaiproject/site/tool
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 15:03:18 2008
X-DSPAM-Confidence: 0.7626
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39766

Author: zqian@umich.edu
Date: 2008-01-04 15:01:37 -0500 (Fri, 04 Jan 2008)
New Revision: 39766

Modified:
site-manage/branches/sakai_2-4-x/site-manage-tool/tool/src/java/org/sakaiproject/site/tool/SiteAction.java
Log:
merge fix to SAK-10788 into site-manage 2.4.x branch:

Sakai Source Repository  	#38024  	Wed Nov 07 14:54:46 MST 2007  	zqian@umich.edu  	 Fix to SAK-10788: If a provided id in a couse site is fake or doesn't provide any user information, Site Info appears to be like project site with empty participant list

Watch for enrollments object being null and concatenate provider ids when there are more than one.
Files Changed
MODIFY /site-manage/trunk/site-manage-tool/tool/src/java/org/sakaiproject/site/tool/SiteAction.java 




----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From rjlowe@iupui.edu Fri Jan  4 14:50:18 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.93])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 14:50:18 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 14:50:18 -0500
Received: from eyewitness.mr.itd.umich.edu (eyewitness.mr.itd.umich.edu [141.211.93.142])
	by mission.mail.umich.edu () with ESMTP id m04JoHJi019755;
	Fri, 4 Jan 2008 14:50:17 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY eyewitness.mr.itd.umich.edu ID 477E8DF2.67B91.5278 ; 
	 4 Jan 2008 14:50:13 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 2D1B9BB492;
	Fri,  4 Jan 2008 19:47:10 +0000 (GMT)
Message-ID: <200801041948.m04JmdwO007705@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 960
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 19:46:50 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id B3E6742F4A
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 19:49:51 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m04JmeV9007707
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 14:48:40 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m04JmdwO007705
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 14:48:39 -0500
Date: Fri, 4 Jan 2008 14:48:39 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to rjlowe@iupui.edu using -f
To: source@collab.sakaiproject.org
From: rjlowe@iupui.edu
Subject: [sakai] svn commit: r39765 - in gradebook/trunk/app: business/src/java/org/sakaiproject/tool/gradebook/business business/src/java/org/sakaiproject/tool/gradebook/business/impl ui ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/beans ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/entity ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/params ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/producers ui/src/webapp/WEB-INF ui/src/webapp/WEB-INF/bundle ui/src/webapp/content/templates
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 14:50:18 2008
X-DSPAM-Confidence: 0.7556
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39765

Author: rjlowe@iupui.edu
Date: 2008-01-04 14:48:37 -0500 (Fri, 04 Jan 2008)
New Revision: 39765

Added:
gradebook/trunk/app/ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/beans/AssignmentGradeRecordBean.java
gradebook/trunk/app/ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/beans/AssignmentGradeRecordCreator.java
gradebook/trunk/app/ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/entity/GradebookEntryGradeEntityProvider.java
gradebook/trunk/app/ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/params/GradeGradebookItemViewParams.java
gradebook/trunk/app/ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/producers/GradeGradebookItemProducer.java
gradebook/trunk/app/ui/src/webapp/content/templates/grade-gradebook-item.html
Modified:
gradebook/trunk/app/business/src/java/org/sakaiproject/tool/gradebook/business/GradebookManager.java
gradebook/trunk/app/business/src/java/org/sakaiproject/tool/gradebook/business/impl/GradebookManagerHibernateImpl.java
gradebook/trunk/app/ui/pom.xml
gradebook/trunk/app/ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/beans/GradebookItemBean.java
gradebook/trunk/app/ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/entity/GradebookEntryEntityProvider.java
gradebook/trunk/app/ui/src/java/org/sakaiproject/tool/gradebook/ui/helpers/producers/AddGradebookItemProducer.java
gradebook/trunk/app/ui/src/webapp/WEB-INF/applicationContext.xml
gradebook/trunk/app/ui/src/webapp/WEB-INF/bundle/messages.properties
gradebook/trunk/app/ui/src/webapp/WEB-INF/requestContext.xml
Log:
SAK-12180 - New helper tool to grade an assignment

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From cwen@iupui.edu Fri Jan  4 11:37:30 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.46])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 11:37:30 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 11:37:30 -0500
Received: from tadpole.mr.itd.umich.edu (tadpole.mr.itd.umich.edu [141.211.14.72])
	by fan.mail.umich.edu () with ESMTP id m04GbT9x022078;
	Fri, 4 Jan 2008 11:37:29 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY tadpole.mr.itd.umich.edu ID 477E60B2.82756.9904 ; 
	 4 Jan 2008 11:37:09 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 8D13DBB001;
	Fri,  4 Jan 2008 16:37:07 +0000 (GMT)
Message-ID: <200801041635.m04GZQGZ007313@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 120
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 16:36:40 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id D430B42E42
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 16:36:37 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m04GZQ7W007315
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 11:35:26 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m04GZQGZ007313
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 11:35:26 -0500
Date: Fri, 4 Jan 2008 11:35:26 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to cwen@iupui.edu using -f
To: source@collab.sakaiproject.org
From: cwen@iupui.edu
Subject: [sakai] svn commit: r39764 - in msgcntr/trunk/messageforums-app/src/java/org/sakaiproject/tool/messageforums: . ui
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 11:37:30 2008
X-DSPAM-Confidence: 0.7002
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39764

Author: cwen@iupui.edu
Date: 2008-01-04 11:35:25 -0500 (Fri, 04 Jan 2008)
New Revision: 39764

Modified:
msgcntr/trunk/messageforums-app/src/java/org/sakaiproject/tool/messageforums/PrivateMessagesTool.java
msgcntr/trunk/messageforums-app/src/java/org/sakaiproject/tool/messageforums/ui/PrivateMessageDecoratedBean.java
Log:
unmerge Xingtang's checkin for SAK-12488.

svn merge -r39558:39557 https://source.sakaiproject.org/svn/msgcntr/trunk
U    messageforums-app/src/java/org/sakaiproject/tool/messageforums/PrivateMessagesTool.java
U    messageforums-app/src/java/org/sakaiproject/tool/messageforums/ui/PrivateMessageDecoratedBean.java

svn log -r 39558
------------------------------------------------------------------------
r39558 | hu2@iupui.edu | 2007-12-20 15:25:38 -0500 (Thu, 20 Dec 2007) | 3 lines

SAK-12488
when send a message to yourself. click reply to all, cc row should be null.
http://jira.sakaiproject.org/jira/browse/SAK-12488
------------------------------------------------------------------------


----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From cwen@iupui.edu Fri Jan  4 11:35:08 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.46])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 11:35:08 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 11:35:08 -0500
Received: from it.mr.itd.umich.edu (it.mr.itd.umich.edu [141.211.93.151])
	by fan.mail.umich.edu () with ESMTP id m04GZ6lt020480;
	Fri, 4 Jan 2008 11:35:06 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY it.mr.itd.umich.edu ID 477E6033.6469D.21870 ; 
	 4 Jan 2008 11:35:02 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id E40FABAE5B;
	Fri,  4 Jan 2008 16:34:38 +0000 (GMT)
Message-ID: <200801041633.m04GX6eG007292@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 697
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 16:34:01 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 1CD0C42E42
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 16:34:17 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m04GX6Y3007294
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 11:33:06 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m04GX6eG007292
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 11:33:06 -0500
Date: Fri, 4 Jan 2008 11:33:06 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to cwen@iupui.edu using -f
To: source@collab.sakaiproject.org
From: cwen@iupui.edu
Subject: [sakai] svn commit: r39763 - in msgcntr/trunk: messageforums-api/src/bundle/org/sakaiproject/api/app/messagecenter/bundle messageforums-app/src/java/org/sakaiproject/tool/messageforums
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 11:35:08 2008
X-DSPAM-Confidence: 0.7615
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39763

Author: cwen@iupui.edu
Date: 2008-01-04 11:33:05 -0500 (Fri, 04 Jan 2008)
New Revision: 39763

Modified:
msgcntr/trunk/messageforums-api/src/bundle/org/sakaiproject/api/app/messagecenter/bundle/Messages.properties
msgcntr/trunk/messageforums-app/src/java/org/sakaiproject/tool/messageforums/PrivateMessagesTool.java
Log:
unmerge Xingtang's check in for SAK-12484.

svn merge -r39571:39570 https://source.sakaiproject.org/svn/msgcntr/trunk
U    messageforums-api/src/bundle/org/sakaiproject/api/app/messagecenter/bundle/Messages.properties
U    messageforums-app/src/java/org/sakaiproject/tool/messageforums/PrivateMessagesTool.java

svn log -r 39571
------------------------------------------------------------------------
r39571 | hu2@iupui.edu | 2007-12-20 21:26:28 -0500 (Thu, 20 Dec 2007) | 3 lines

SAK-12484
reply all cc list should not include the current user name.
http://jira.sakaiproject.org/jira/browse/SAK-12484
------------------------------------------------------------------------


----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From gsilver@umich.edu Fri Jan  4 11:12:37 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.25])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 11:12:37 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 11:12:37 -0500
Received: from holes.mr.itd.umich.edu (holes.mr.itd.umich.edu [141.211.14.79])
	by panther.mail.umich.edu () with ESMTP id m04GCaHB030887;
	Fri, 4 Jan 2008 11:12:36 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY holes.mr.itd.umich.edu ID 477E5AEB.E670B.28397 ; 
	 4 Jan 2008 11:12:30 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 99715BAE7D;
	Fri,  4 Jan 2008 16:12:27 +0000 (GMT)
Message-ID: <200801041611.m04GB1Lb007221@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 272
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 16:12:14 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 0A6ED42DFC
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 16:12:12 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m04GB1Wt007223
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 11:11:01 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m04GB1Lb007221
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 11:11:01 -0500
Date: Fri, 4 Jan 2008 11:11:01 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to gsilver@umich.edu using -f
To: source@collab.sakaiproject.org
From: gsilver@umich.edu
Subject: [sakai] svn commit: r39762 - web/trunk/web-tool/tool/src/bundle
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 11:12:37 2008
X-DSPAM-Confidence: 0.7601
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39762

Author: gsilver@umich.edu
Date: 2008-01-04 11:11:00 -0500 (Fri, 04 Jan 2008)
New Revision: 39762

Modified:
web/trunk/web-tool/tool/src/bundle/iframe.properties
Log:
SAK-12596
http://bugs.sakaiproject.org/jira/browse/SAK-12596
- left moot (unused) entries commented for now

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From gsilver@umich.edu Fri Jan  4 11:11:52 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.36])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 11:11:52 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 11:11:52 -0500
Received: from creepshow.mr.itd.umich.edu (creepshow.mr.itd.umich.edu [141.211.14.84])
	by godsend.mail.umich.edu () with ESMTP id m04GBqqv025330;
	Fri, 4 Jan 2008 11:11:52 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY creepshow.mr.itd.umich.edu ID 477E5AB3.5CC32.30840 ; 
	 4 Jan 2008 11:11:34 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 62AA4BAE46;
	Fri,  4 Jan 2008 16:11:31 +0000 (GMT)
Message-ID: <200801041610.m04GA5KP007209@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 1006
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 16:11:18 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id C596A3DFA2
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 16:11:16 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m04GA5LR007211
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 11:10:05 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m04GA5KP007209
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 11:10:05 -0500
Date: Fri, 4 Jan 2008 11:10:05 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to gsilver@umich.edu using -f
To: source@collab.sakaiproject.org
From: gsilver@umich.edu
Subject: [sakai] svn commit: r39761 - site/trunk/site-tool/tool/src/bundle
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 11:11:52 2008
X-DSPAM-Confidence: 0.7605
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39761

Author: gsilver@umich.edu
Date: 2008-01-04 11:10:04 -0500 (Fri, 04 Jan 2008)
New Revision: 39761

Modified:
site/trunk/site-tool/tool/src/bundle/admin.properties
Log:
SAK-12595
http://bugs.sakaiproject.org/jira/browse/SAK-12595
- left moot (unused) entries commented for now

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From zqian@umich.edu Fri Jan  4 11:11:03 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.97])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 11:11:03 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 11:11:03 -0500
Received: from carrie.mr.itd.umich.edu (carrie.mr.itd.umich.edu [141.211.93.152])
	by sleepers.mail.umich.edu () with ESMTP id m04GB3Vg011502;
	Fri, 4 Jan 2008 11:11:03 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY carrie.mr.itd.umich.edu ID 477E5A8D.B378F.24200 ; 
	 4 Jan 2008 11:10:56 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id C7251BAD44;
	Fri,  4 Jan 2008 16:10:53 +0000 (GMT)
Message-ID: <200801041609.m04G9EuX007197@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 483
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 16:10:27 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 2E7043DFA2
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 16:10:26 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m04G9Eqg007199
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 11:09:15 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m04G9EuX007197
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 11:09:14 -0500
Date: Fri, 4 Jan 2008 11:09:14 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to zqian@umich.edu using -f
To: source@collab.sakaiproject.org
From: zqian@umich.edu
Subject: [sakai] svn commit: r39760 - in site-manage/trunk/site-manage-tool/tool/src: java/org/sakaiproject/site/tool webapp/vm/sitesetup
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 11:11:03 2008
X-DSPAM-Confidence: 0.6959
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39760

Author: zqian@umich.edu
Date: 2008-01-04 11:09:12 -0500 (Fri, 04 Jan 2008)
New Revision: 39760

Modified:
site-manage/trunk/site-manage-tool/tool/src/java/org/sakaiproject/site/tool/SiteAction.java
site-manage/trunk/site-manage-tool/tool/src/webapp/vm/sitesetup/chef_site-siteInfo-list.vm
Log:
fix to SAK-10911: Refactor use of site.upd, site.upd.site.mbrship and site.upd.grp.mbrship permissions

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From gsilver@umich.edu Fri Jan  4 11:10:22 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.39])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 11:10:22 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 11:10:22 -0500
Received: from holes.mr.itd.umich.edu (holes.mr.itd.umich.edu [141.211.14.79])
	by faithful.mail.umich.edu () with ESMTP id m04GAL9k010604;
	Fri, 4 Jan 2008 11:10:21 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY holes.mr.itd.umich.edu ID 477E5A67.34350.23015 ; 
	 4 Jan 2008 11:10:18 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 98D04BAD43;
	Fri,  4 Jan 2008 16:10:11 +0000 (GMT)
Message-ID: <200801041608.m04G8d7w007184@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 966
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 16:09:51 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 9F89542DD0
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 16:09:50 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m04G8dXN007186
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 11:08:39 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m04G8d7w007184
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 11:08:39 -0500
Date: Fri, 4 Jan 2008 11:08:39 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to gsilver@umich.edu using -f
To: source@collab.sakaiproject.org
From: gsilver@umich.edu
Subject: [sakai] svn commit: r39759 - mailarchive/trunk/mailarchive-tool/tool/src/bundle
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 11:10:22 2008
X-DSPAM-Confidence: 0.7606
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39759

Author: gsilver@umich.edu
Date: 2008-01-04 11:08:38 -0500 (Fri, 04 Jan 2008)
New Revision: 39759

Modified:
mailarchive/trunk/mailarchive-tool/tool/src/bundle/email.properties
Log:
SAK-12592
http://bugs.sakaiproject.org/jira/browse/SAK-12592
- left moot (unused) entries commented for now

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From wagnermr@iupui.edu Fri Jan  4 10:38:42 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.90])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 10:38:42 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 10:38:42 -0500
Received: from shining.mr.itd.umich.edu (shining.mr.itd.umich.edu [141.211.93.153])
	by flawless.mail.umich.edu () with ESMTP id m04Fcfjm012313;
	Fri, 4 Jan 2008 10:38:41 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY shining.mr.itd.umich.edu ID 477E52FA.E6C6E.24093 ; 
	 4 Jan 2008 10:38:37 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 6A39594CD2;
	Fri,  4 Jan 2008 15:37:36 +0000 (GMT)
Message-ID: <200801041537.m04Fb6Ci007092@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 690
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 15:37:21 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id CEFA037ACE
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 15:38:17 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m04Fb6nh007094
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 10:37:06 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m04Fb6Ci007092
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 10:37:06 -0500
Date: Fri, 4 Jan 2008 10:37:06 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to wagnermr@iupui.edu using -f
To: source@collab.sakaiproject.org
From: wagnermr@iupui.edu
Subject: [sakai] svn commit: r39758 - in gradebook/trunk: app/business/src/java/org/sakaiproject/tool/gradebook/business/impl service/api/src/java/org/sakaiproject/service/gradebook/shared service/impl/src/java/org/sakaiproject/component/gradebook
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 10:38:42 2008
X-DSPAM-Confidence: 0.7559
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39758

Author: wagnermr@iupui.edu
Date: 2008-01-04 10:37:04 -0500 (Fri, 04 Jan 2008)
New Revision: 39758

Modified:
gradebook/trunk/app/business/src/java/org/sakaiproject/tool/gradebook/business/impl/GradebookManagerHibernateImpl.java
gradebook/trunk/service/api/src/java/org/sakaiproject/service/gradebook/shared/GradebookService.java
gradebook/trunk/service/impl/src/java/org/sakaiproject/component/gradebook/GradebookServiceHibernateImpl.java
Log:
SAK-12175
http://bugs.sakaiproject.org/jira/browse/SAK-12175
Create methods required for gb integration with the Assignment2 tool
getGradeDefinitionForStudentForItem

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From zqian@umich.edu Fri Jan  4 10:17:43 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.97])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 10:17:43 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 10:17:42 -0500
Received: from creepshow.mr.itd.umich.edu (creepshow.mr.itd.umich.edu [141.211.14.84])
	by sleepers.mail.umich.edu () with ESMTP id m04FHgfs011536;
	Fri, 4 Jan 2008 10:17:42 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY creepshow.mr.itd.umich.edu ID 477E4E0F.CCA4B.926 ; 
	 4 Jan 2008 10:17:38 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id BD02DBAC64;
	Fri,  4 Jan 2008 15:17:34 +0000 (GMT)
Message-ID: <200801041515.m04FFv42007050@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 25
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 15:17:11 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 5B396236B9
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 15:17:08 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m04FFv85007052
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 10:15:57 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m04FFv42007050
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 10:15:57 -0500
Date: Fri, 4 Jan 2008 10:15:57 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to zqian@umich.edu using -f
To: source@collab.sakaiproject.org
From: zqian@umich.edu
Subject: [sakai] svn commit: r39757 - in assignment/trunk: assignment-impl/impl/src/java/org/sakaiproject/assignment/impl assignment-tool/tool/src/webapp/vm/assignment
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 10:17:42 2008
X-DSPAM-Confidence: 0.7605
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39757

Author: zqian@umich.edu
Date: 2008-01-04 10:15:54 -0500 (Fri, 04 Jan 2008)
New Revision: 39757

Modified:
assignment/trunk/assignment-impl/impl/src/java/org/sakaiproject/assignment/impl/BaseAssignmentService.java
assignment/trunk/assignment-tool/tool/src/webapp/vm/assignment/chef_assignments_instructor_list_submissions.vm
Log:
fix to SAK-12604:Don't show groups/sections filter if the site doesn't have any

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From antranig@caret.cam.ac.uk Fri Jan  4 10:04:14 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.25])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 10:04:14 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 10:04:14 -0500
Received: from holes.mr.itd.umich.edu (holes.mr.itd.umich.edu [141.211.14.79])
	by panther.mail.umich.edu () with ESMTP id m04F4Dci015108;
	Fri, 4 Jan 2008 10:04:13 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY holes.mr.itd.umich.edu ID 477E4AE3.D7AF.31669 ; 
	 4 Jan 2008 10:04:05 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 933E3BAC17;
	Fri,  4 Jan 2008 15:04:00 +0000 (GMT)
Message-ID: <200801041502.m04F21Jo007031@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 32
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 15:03:15 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id AC2F6236B9
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 15:03:12 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m04F21hn007033
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 10:02:01 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m04F21Jo007031
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 10:02:01 -0500
Date: Fri, 4 Jan 2008 10:02:01 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to antranig@caret.cam.ac.uk using -f
To: source@collab.sakaiproject.org
From: antranig@caret.cam.ac.uk
Subject: [sakai] svn commit: r39756 - in component/branches/SAK-12166/component-api/component/src/java/org/sakaiproject/component: impl impl/spring/support impl/spring/support/dynamic impl/support util
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 10:04:14 2008
X-DSPAM-Confidence: 0.6932
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39756

Author: antranig@caret.cam.ac.uk
Date: 2008-01-04 10:01:40 -0500 (Fri, 04 Jan 2008)
New Revision: 39756

Added:
component/branches/SAK-12166/component-api/component/src/java/org/sakaiproject/component/impl/spring/support/dynamic/
component/branches/SAK-12166/component-api/component/src/java/org/sakaiproject/component/impl/spring/support/dynamic/DynamicComponentManager.java
component/branches/SAK-12166/component-api/component/src/java/org/sakaiproject/component/impl/support/
component/branches/SAK-12166/component-api/component/src/java/org/sakaiproject/component/impl/support/DynamicComponentRecord.java
component/branches/SAK-12166/component-api/component/src/java/org/sakaiproject/component/impl/support/DynamicJARManager.java
component/branches/SAK-12166/component-api/component/src/java/org/sakaiproject/component/impl/support/JARRecord.java
component/branches/SAK-12166/component-api/component/src/java/org/sakaiproject/component/util/ByteToCharBase64.java
component/branches/SAK-12166/component-api/component/src/java/org/sakaiproject/component/util/FileUtil.java
component/branches/SAK-12166/component-api/component/src/java/org/sakaiproject/component/util/RecordFileIO.java
component/branches/SAK-12166/component-api/component/src/java/org/sakaiproject/component/util/RecordReader.java
component/branches/SAK-12166/component-api/component/src/java/org/sakaiproject/component/util/RecordWriter.java
component/branches/SAK-12166/component-api/component/src/java/org/sakaiproject/component/util/StreamDigestor.java
Modified:
component/branches/SAK-12166/component-api/component/src/java/org/sakaiproject/component/impl/spring/support/ComponentsLoaderImpl.java
Log:
Temporary commit of incomplete work on JAR caching

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From gopal.ramasammycook@gmail.com Fri Jan  4 09:05:31 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.90])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 09:05:31 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 09:05:31 -0500
Received: from guys.mr.itd.umich.edu (guys.mr.itd.umich.edu [141.211.14.76])
	by flawless.mail.umich.edu () with ESMTP id m04E5U3C029277;
	Fri, 4 Jan 2008 09:05:30 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY guys.mr.itd.umich.edu ID 477E3D23.EE2E7.5237 ; 
	 4 Jan 2008 09:05:26 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 33C7856DC0;
	Fri,  4 Jan 2008 14:05:26 +0000 (GMT)
Message-ID: <200801041403.m04E3psW006926@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 575
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 14:05:04 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 3C0261D617
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 14:05:03 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m04E3pQS006928
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 09:03:52 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m04E3psW006926
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 09:03:51 -0500
Date: Fri, 4 Jan 2008 09:03:51 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to gopal.ramasammycook@gmail.com using -f
To: source@collab.sakaiproject.org
From: gopal.ramasammycook@gmail.com
Subject: [sakai] svn commit: r39755 - in sam/branches/SAK-12065: samigo-api/src/java/org/sakaiproject/tool/assessment/shared/api/grading samigo-app/src/java/org/sakaiproject/tool/assessment/ui/bean/evaluation samigo-app/src/java/org/sakaiproject/tool/assessment/ui/listener/evaluation samigo-services/src/java/org/sakaiproject/tool/assessment/facade samigo-services/src/java/org/sakaiproject/tool/assessment/integration/helper/ifc samigo-services/src/java/org/sakaiproject/tool/assessment/integration/helper/integrated samigo-services/src/java/org/sakaiproject/tool/assessment/integration/helper/standalone samigo-services/src/java/org/sakaiproject/tool/assessment/shared/impl/grading
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 09:05:31 2008
X-DSPAM-Confidence: 0.7558
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39755

Author: gopal.ramasammycook@gmail.com
Date: 2008-01-04 09:02:54 -0500 (Fri, 04 Jan 2008)
New Revision: 39755

Modified:
sam/branches/SAK-12065/samigo-api/src/java/org/sakaiproject/tool/assessment/shared/api/grading/GradingSectionAwareServiceAPI.java
sam/branches/SAK-12065/samigo-app/src/java/org/sakaiproject/tool/assessment/ui/bean/evaluation/QuestionScoresBean.java
sam/branches/SAK-12065/samigo-app/src/java/org/sakaiproject/tool/assessment/ui/bean/evaluation/SubmissionStatusBean.java
sam/branches/SAK-12065/samigo-app/src/java/org/sakaiproject/tool/assessment/ui/bean/evaluation/TotalScoresBean.java
sam/branches/SAK-12065/samigo-app/src/java/org/sakaiproject/tool/assessment/ui/listener/evaluation/SubmissionStatusListener.java
sam/branches/SAK-12065/samigo-services/src/java/org/sakaiproject/tool/assessment/facade/PublishedAssessmentFacadeQueries.java
sam/branches/SAK-12065/samigo-services/src/java/org/sakaiproject/tool/assessment/facade/PublishedAssessmentFacadeQueriesAPI.java
sam/branches/SAK-12065/samigo-services/src/java/org/sakaiproject/tool/assessment/integration/helper/ifc/SectionAwareServiceHelper.java
sam/branches/SAK-12065/samigo-services/src/java/org/sakaiproject/tool/assessment/integration/helper/integrated/SectionAwareServiceHelperImpl.java
sam/branches/SAK-12065/samigo-services/src/java/org/sakaiproject/tool/assessment/integration/helper/standalone/SectionAwareServiceHelperImpl.java
sam/branches/SAK-12065/samigo-services/src/java/org/sakaiproject/tool/assessment/shared/impl/grading/GradingSectionAwareServiceImpl.java
Log:
SAK-12065 Gopal - Samigo Group Release. SubmissionStatus/TotalScores/Questions View filter.

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From david.horwitz@uct.ac.za Fri Jan  4 07:02:32 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.39])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 07:02:32 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 07:02:32 -0500
Received: from guys.mr.itd.umich.edu (guys.mr.itd.umich.edu [141.211.14.76])
	by faithful.mail.umich.edu () with ESMTP id m04C2VN7026678;
	Fri, 4 Jan 2008 07:02:31 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY guys.mr.itd.umich.edu ID 477E2050.C2599.3263 ; 
	 4 Jan 2008 07:02:27 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 6497FBA906;
	Fri,  4 Jan 2008 12:02:11 +0000 (GMT)
Message-ID: <200801041200.m04C0gfK006793@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 611
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 12:01:53 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 5296342D3C
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 12:01:53 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m04C0gnm006795
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 07:00:42 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m04C0gfK006793
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 07:00:42 -0500
Date: Fri, 4 Jan 2008 07:00:42 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
To: source@collab.sakaiproject.org
From: david.horwitz@uct.ac.za
Subject: [sakai] svn commit: r39754 - in polls/branches/sakai_2-5-x: . tool tool/src/java/org/sakaiproject/poll/tool tool/src/java/org/sakaiproject/poll/tool/evolvers tool/src/webapp/WEB-INF
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 07:02:32 2008
X-DSPAM-Confidence: 0.6526
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39754

Author: david.horwitz@uct.ac.za
Date: 2008-01-04 07:00:10 -0500 (Fri, 04 Jan 2008)
New Revision: 39754

Added:
polls/branches/sakai_2-5-x/tool/src/java/org/sakaiproject/poll/tool/evolvers/
polls/branches/sakai_2-5-x/tool/src/java/org/sakaiproject/poll/tool/evolvers/SakaiFCKTextEvolver.java
Removed:
polls/branches/sakai_2-5-x/tool/src/java/org/sakaiproject/poll/tool/evolvers/SakaiFCKTextEvolver.java
Modified:
polls/branches/sakai_2-5-x/.classpath
polls/branches/sakai_2-5-x/tool/pom.xml
polls/branches/sakai_2-5-x/tool/src/webapp/WEB-INF/requestContext.xml
Log:
svn log -r39753 https://source.sakaiproject.org/svn/polls/trunk
------------------------------------------------------------------------
r39753 | david.horwitz@uct.ac.za | 2008-01-04 13:05:51 +0200 (Fri, 04 Jan 2008) | 1 line

SAK-12228 implmented workaround sugested by AB - needs to be tested against a trunk build
------------------------------------------------------------------------
dhorwitz@david-horwitz-6:~/branchManagemnt/sakai_2-5-x> svn merge -c39753 https://source.sakaiproject.org/svn/polls/trunk polls/
U    polls/.classpath
A    polls/tool/src/java/org/sakaiproject/poll/tool/evolvers
A    polls/tool/src/java/org/sakaiproject/poll/tool/evolvers/SakaiFCKTextEvolver.java
C    polls/tool/src/webapp/WEB-INF/requestContext.xml
U    polls/tool/pom.xml

dhorwitz@david-horwitz-6:~/branchManagemnt/sakai_2-5-x> svn resolved polls/tool/src/webapp/WEB-INF/requestContext.xml
Resolved conflicted state of 'polls/tool/src/webapp/WEB-INF/requestContext.xml


----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From david.horwitz@uct.ac.za Fri Jan  4 06:08:27 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.98])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 06:08:27 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 06:08:27 -0500
Received: from firestarter.mr.itd.umich.edu (firestarter.mr.itd.umich.edu [141.211.14.83])
	by casino.mail.umich.edu () with ESMTP id m04B8Qw9001368;
	Fri, 4 Jan 2008 06:08:26 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY firestarter.mr.itd.umich.edu ID 477E13A5.30FC0.24054 ; 
	 4 Jan 2008 06:08:23 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 784A476D7B;
	Fri,  4 Jan 2008 11:08:12 +0000 (GMT)
Message-ID: <200801041106.m04B6lK3006677@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 585
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 11:07:56 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 1CACC42D0C
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 11:07:58 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m04B6lWM006679
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 06:06:47 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m04B6lK3006677
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 06:06:47 -0500
Date: Fri, 4 Jan 2008 06:06:47 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
To: source@collab.sakaiproject.org
From: david.horwitz@uct.ac.za
Subject: [sakai] svn commit: r39753 - in polls/trunk: . tool tool/src/java/org/sakaiproject/poll/tool tool/src/java/org/sakaiproject/poll/tool/evolvers tool/src/webapp/WEB-INF
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 06:08:27 2008
X-DSPAM-Confidence: 0.6948
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39753

Author: david.horwitz@uct.ac.za
Date: 2008-01-04 06:05:51 -0500 (Fri, 04 Jan 2008)
New Revision: 39753

Added:
polls/trunk/tool/src/java/org/sakaiproject/poll/tool/evolvers/
polls/trunk/tool/src/java/org/sakaiproject/poll/tool/evolvers/SakaiFCKTextEvolver.java
Modified:
polls/trunk/.classpath
polls/trunk/tool/pom.xml
polls/trunk/tool/src/webapp/WEB-INF/requestContext.xml
Log:
SAK-12228 implmented workaround sugested by AB - needs to be tested against a trunk build

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From david.horwitz@uct.ac.za Fri Jan  4 04:49:08 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.92])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 04:49:08 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 04:49:08 -0500
Received: from galaxyquest.mr.itd.umich.edu (galaxyquest.mr.itd.umich.edu [141.211.93.145])
	by score.mail.umich.edu () with ESMTP id m049n60G017588;
	Fri, 4 Jan 2008 04:49:06 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY galaxyquest.mr.itd.umich.edu ID 477E010C.48C2.10259 ; 
	 4 Jan 2008 04:49:03 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 254CC8CDEE;
	Fri,  4 Jan 2008 09:48:55 +0000 (GMT)
Message-ID: <200801040947.m049lUxo006517@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 246
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 09:48:36 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 8C13342C92
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 09:48:40 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m049lU3P006519
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 04:47:30 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m049lUxo006517
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 04:47:30 -0500
Date: Fri, 4 Jan 2008 04:47:30 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
To: source@collab.sakaiproject.org
From: david.horwitz@uct.ac.za
Subject: [sakai] svn commit: r39752 - in podcasts/branches/sakai_2-5-x/podcasts-app/src/webapp: css podcasts
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 04:49:08 2008
X-DSPAM-Confidence: 0.6528
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39752

Author: david.horwitz@uct.ac.za
Date: 2008-01-04 04:47:16 -0500 (Fri, 04 Jan 2008)
New Revision: 39752

Modified:
podcasts/branches/sakai_2-5-x/podcasts-app/src/webapp/css/podcaster.css
podcasts/branches/sakai_2-5-x/podcasts-app/src/webapp/podcasts/podMain.jsp
Log:
svn log -r39641 https://source.sakaiproject.org/svn/podcasts/trunk
------------------------------------------------------------------------
r39641 | josrodri@iupui.edu | 2007-12-28 23:44:24 +0200 (Fri, 28 Dec 2007) | 1 line

SAK-9882: refactored podMain.jsp the right way (at least much closer to)
------------------------------------------------------------------------

dhorwitz@david-horwitz-6:~/branchManagemnt/sakai_2-5-x> svn merge  -c39641 https://source.sakaiproject.org/svn/podcasts/trunk podcasts/
C    podcasts/podcasts-app/src/webapp/podcasts/podMain.jsp
U    podcasts/podcasts-app/src/webapp/css/podcaster.css

conflict merged manualy



----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From david.horwitz@uct.ac.za Fri Jan  4 04:33:44 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.46])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 04:33:44 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 04:33:44 -0500
Received: from workinggirl.mr.itd.umich.edu (workinggirl.mr.itd.umich.edu [141.211.93.143])
	by fan.mail.umich.edu () with ESMTP id m049Xge3031803;
	Fri, 4 Jan 2008 04:33:42 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY workinggirl.mr.itd.umich.edu ID 477DFD6C.75DBE.26054 ; 
	 4 Jan 2008 04:33:35 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 6C929BA656;
	Fri,  4 Jan 2008 09:33:27 +0000 (GMT)
Message-ID: <200801040932.m049W2i5006493@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 153
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 09:33:10 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 6C69423767
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 09:33:13 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m049W3fl006495
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 04:32:03 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m049W2i5006493
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 04:32:02 -0500
Date: Fri, 4 Jan 2008 04:32:02 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to david.horwitz@uct.ac.za using -f
To: source@collab.sakaiproject.org
From: david.horwitz@uct.ac.za
Subject: [sakai] svn commit: r39751 - in podcasts/branches/sakai_2-5-x/podcasts-app/src/webapp: css images podcasts
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 04:33:44 2008
X-DSPAM-Confidence: 0.7002
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39751

Author: david.horwitz@uct.ac.za
Date: 2008-01-04 04:31:35 -0500 (Fri, 04 Jan 2008)
New Revision: 39751

Removed:
podcasts/branches/sakai_2-5-x/podcasts-app/src/webapp/images/rss-feed-icon.png
podcasts/branches/sakai_2-5-x/podcasts-app/src/webapp/podcasts/podPermissions.jsp
Modified:
podcasts/branches/sakai_2-5-x/podcasts-app/src/webapp/css/podcaster.css
podcasts/branches/sakai_2-5-x/podcasts-app/src/webapp/podcasts/podDelete.jsp
podcasts/branches/sakai_2-5-x/podcasts-app/src/webapp/podcasts/podMain.jsp
podcasts/branches/sakai_2-5-x/podcasts-app/src/webapp/podcasts/podNoResource.jsp
podcasts/branches/sakai_2-5-x/podcasts-app/src/webapp/podcasts/podOptions.jsp
Log:
svn log -r39146 https://source.sakaiproject.org/svn/podcasts/trunk
------------------------------------------------------------------------
r39146 | josrodri@iupui.edu | 2007-12-12 21:40:33 +0200 (Wed, 12 Dec 2007) | 1 line

SAK-9882: refactored the other pages as well to take advantage of proper jsp components as well as validation cleanup.
------------------------------------------------------------------------
dhorwitz@david-horwitz-6:~/branchManagemnt/sakai_2-5-x> svn merge -c39146 https://source.sakaiproject.org/svn/podcasts/trunk podcasts/
D    podcasts/podcasts-app/src/webapp/podcasts/podPermissions.jsp
U    podcasts/podcasts-app/src/webapp/podcasts/podDelete.jsp
U    podcasts/podcasts-app/src/webapp/podcasts/podMain.jsp
U    podcasts/podcasts-app/src/webapp/podcasts/podNoResource.jsp
U    podcasts/podcasts-app/src/webapp/podcasts/podOptions.jsp
D    podcasts/podcasts-app/src/webapp/images/rss-feed-icon.png
U    podcasts/podcasts-app/src/webapp/css/podcaster.css



----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.25])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Fri, 04 Jan 2008 04:07:34 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Fri, 04 Jan 2008 04:07:34 -0500
Received: from salemslot.mr.itd.umich.edu (salemslot.mr.itd.umich.edu [141.211.14.58])
	by panther.mail.umich.edu () with ESMTP id m0497WAN027902;
	Fri, 4 Jan 2008 04:07:32 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY salemslot.mr.itd.umich.edu ID 477DF74E.49493.30415 ; 
	 4 Jan 2008 04:07:29 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 88598BA5B6;
	Fri,  4 Jan 2008 09:07:19 +0000 (GMT)
Message-ID: <200801040905.m0495rWB006420@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 385
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 09:07:04 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 90636418A8
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 09:07:04 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m0495sZs006422
	for <source@collab.sakaiproject.org>; Fri, 4 Jan 2008 04:05:54 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m0495rWB006420
	for source@collab.sakaiproject.org; Fri, 4 Jan 2008 04:05:53 -0500
Date: Fri, 4 Jan 2008 04:05:53 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to stephen.marquard@uct.ac.za using -f
To: source@collab.sakaiproject.org
From: stephen.marquard@uct.ac.za
Subject: [sakai] svn commit: r39750 - event/branches/SAK-6216/event-util/util/src/java/org/sakaiproject/util
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Fri Jan  4 04:07:34 2008
X-DSPAM-Confidence: 0.7554
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39750

Author: stephen.marquard@uct.ac.za
Date: 2008-01-04 04:05:43 -0500 (Fri, 04 Jan 2008)
New Revision: 39750

Modified:
event/branches/SAK-6216/event-util/util/src/java/org/sakaiproject/util/EmailNotification.java
Log:
SAK-6216 merge event change from SAK-11169 (r39033) to synchronize branch with 2-5-x (for convenience for UCT local build)

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From louis@media.berkeley.edu Thu Jan  3 19:51:21 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.91])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Thu, 03 Jan 2008 19:51:21 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Thu, 03 Jan 2008 19:51:21 -0500
Received: from eyewitness.mr.itd.umich.edu (eyewitness.mr.itd.umich.edu [141.211.93.142])
	by jacknife.mail.umich.edu () with ESMTP id m040pJHB027171;
	Thu, 3 Jan 2008 19:51:19 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY eyewitness.mr.itd.umich.edu ID 477D8300.AC098.32562 ; 
	 3 Jan 2008 19:51:15 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id E6CC4B9F8A;
	Fri,  4 Jan 2008 00:36:06 +0000 (GMT)
Message-ID: <200801040023.m040NpCc005473@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 754
          for <source@collab.sakaiproject.org>;
          Fri, 4 Jan 2008 00:35:43 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 8889842C49
	for <source@collab.sakaiproject.org>; Fri,  4 Jan 2008 00:25:00 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m040NpgM005475
	for <source@collab.sakaiproject.org>; Thu, 3 Jan 2008 19:23:51 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m040NpCc005473
	for source@collab.sakaiproject.org; Thu, 3 Jan 2008 19:23:51 -0500
Date: Thu, 3 Jan 2008 19:23:51 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to louis@media.berkeley.edu using -f
To: source@collab.sakaiproject.org
From: louis@media.berkeley.edu
Subject: [sakai] svn commit: r39749 - in bspace/site-manage/sakai_2-4-x/site-manage-tool/tool/src: bundle webapp/vm/sitesetup
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Thu Jan  3 19:51:20 2008
X-DSPAM-Confidence: 0.6956
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39749

Author: louis@media.berkeley.edu
Date: 2008-01-03 19:23:46 -0500 (Thu, 03 Jan 2008)
New Revision: 39749

Modified:
bspace/site-manage/sakai_2-4-x/site-manage-tool/tool/src/bundle/sitesetupgeneric.properties
bspace/site-manage/sakai_2-4-x/site-manage-tool/tool/src/webapp/vm/sitesetup/chef_site-importSites.vm
Log:
BSP-1420 Update text to clarify "Re-Use Materials..." option in WS Setup

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From louis@media.berkeley.edu Thu Jan  3 17:18:23 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.91])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Thu, 03 Jan 2008 17:18:23 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Thu, 03 Jan 2008 17:18:23 -0500
Received: from salemslot.mr.itd.umich.edu (salemslot.mr.itd.umich.edu [141.211.14.58])
	by jacknife.mail.umich.edu () with ESMTP id m03MIMXY027729;
	Thu, 3 Jan 2008 17:18:22 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY salemslot.mr.itd.umich.edu ID 477D5F23.797F6.16348 ; 
	 3 Jan 2008 17:18:14 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id EF439B98CE;
	Thu,  3 Jan 2008 22:18:19 +0000 (GMT)
Message-ID: <200801032216.m03MGhDa005292@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 236
          for <source@collab.sakaiproject.org>;
          Thu, 3 Jan 2008 22:18:04 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 905D53C2FD
	for <source@collab.sakaiproject.org>; Thu,  3 Jan 2008 22:17:52 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m03MGhrs005294
	for <source@collab.sakaiproject.org>; Thu, 3 Jan 2008 17:16:43 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m03MGhDa005292
	for source@collab.sakaiproject.org; Thu, 3 Jan 2008 17:16:43 -0500
Date: Thu, 3 Jan 2008 17:16:43 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to louis@media.berkeley.edu using -f
To: source@collab.sakaiproject.org
From: louis@media.berkeley.edu
Subject: [sakai] svn commit: r39746 - in bspace/site-manage/sakai_2-4-x/site-manage-tool/tool/src: bundle webapp/vm/sitesetup
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Thu Jan  3 17:18:23 2008
X-DSPAM-Confidence: 0.6959
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39746

Author: louis@media.berkeley.edu
Date: 2008-01-03 17:16:39 -0500 (Thu, 03 Jan 2008)
New Revision: 39746

Modified:
bspace/site-manage/sakai_2-4-x/site-manage-tool/tool/src/bundle/sitesetupgeneric.properties
bspace/site-manage/sakai_2-4-x/site-manage-tool/tool/src/webapp/vm/sitesetup/chef_site-siteInfo-duplicate.vm
Log:
BSP-1421 Add text to clarify "Duplicate Site" option in Site Info

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From ray@media.berkeley.edu Thu Jan  3 17:07:00 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.39])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Thu, 03 Jan 2008 17:07:00 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Thu, 03 Jan 2008 17:07:00 -0500
Received: from anniehall.mr.itd.umich.edu (anniehall.mr.itd.umich.edu [141.211.93.141])
	by faithful.mail.umich.edu () with ESMTP id m03M6xaq014868;
	Thu, 3 Jan 2008 17:06:59 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY anniehall.mr.itd.umich.edu ID 477D5C7A.4FE1F.22211 ; 
	 3 Jan 2008 17:06:53 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 0BC8D7225E;
	Thu,  3 Jan 2008 22:06:57 +0000 (GMT)
Message-ID: <200801032205.m03M5Ea7005273@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 554
          for <source@collab.sakaiproject.org>;
          Thu, 3 Jan 2008 22:06:34 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 2AB513C2FD
	for <source@collab.sakaiproject.org>; Thu,  3 Jan 2008 22:06:23 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m03M5EQa005275
	for <source@collab.sakaiproject.org>; Thu, 3 Jan 2008 17:05:14 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m03M5Ea7005273
	for source@collab.sakaiproject.org; Thu, 3 Jan 2008 17:05:14 -0500
Date: Thu, 3 Jan 2008 17:05:14 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to ray@media.berkeley.edu using -f
To: source@collab.sakaiproject.org
From: ray@media.berkeley.edu
Subject: [sakai] svn commit: r39745 - providers/trunk/cm/cm-authz-provider/src/java/org/sakaiproject/coursemanagement/impl/provider
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Thu Jan  3 17:07:00 2008
X-DSPAM-Confidence: 0.7556
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39745

Author: ray@media.berkeley.edu
Date: 2008-01-03 17:05:11 -0500 (Thu, 03 Jan 2008)
New Revision: 39745

Modified:
providers/trunk/cm/cm-authz-provider/src/java/org/sakaiproject/coursemanagement/impl/provider/CourseManagementGroupProvider.java
Log:
SAK-12602 Fix logic when a user has multiple roles in a section

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From cwen@iupui.edu Thu Jan  3 16:34:40 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.34])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Thu, 03 Jan 2008 16:34:40 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Thu, 03 Jan 2008 16:34:40 -0500
Received: from icestorm.mr.itd.umich.edu (icestorm.mr.itd.umich.edu [141.211.93.149])
	by chaos.mail.umich.edu () with ESMTP id m03LYdY1029538;
	Thu, 3 Jan 2008 16:34:39 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY icestorm.mr.itd.umich.edu ID 477D54EA.13F34.26602 ; 
	 3 Jan 2008 16:34:36 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id CC710ADC79;
	Thu,  3 Jan 2008 21:34:29 +0000 (GMT)
Message-ID: <200801032133.m03LX3gG005191@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 611
          for <source@collab.sakaiproject.org>;
          Thu, 3 Jan 2008 21:34:08 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 43C4242B55
	for <source@collab.sakaiproject.org>; Thu,  3 Jan 2008 21:34:12 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m03LX3Vb005193
	for <source@collab.sakaiproject.org>; Thu, 3 Jan 2008 16:33:03 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m03LX3gG005191
	for source@collab.sakaiproject.org; Thu, 3 Jan 2008 16:33:03 -0500
Date: Thu, 3 Jan 2008 16:33:03 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to cwen@iupui.edu using -f
To: source@collab.sakaiproject.org
From: cwen@iupui.edu
Subject: [sakai] svn commit: r39744 - oncourse/branches/oncourse_OPC_122007
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Thu Jan  3 16:34:40 2008
X-DSPAM-Confidence: 0.9846
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39744

Author: cwen@iupui.edu
Date: 2008-01-03 16:33:02 -0500 (Thu, 03 Jan 2008)
New Revision: 39744

Modified:
oncourse/branches/oncourse_OPC_122007/
oncourse/branches/oncourse_OPC_122007/.externals
Log:
update external for GB.

----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From cwen@iupui.edu Thu Jan  3 16:29:07 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.46])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Thu, 03 Jan 2008 16:29:07 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Thu, 03 Jan 2008 16:29:07 -0500
Received: from galaxyquest.mr.itd.umich.edu (galaxyquest.mr.itd.umich.edu [141.211.93.145])
	by fan.mail.umich.edu () with ESMTP id m03LT6uw027749;
	Thu, 3 Jan 2008 16:29:06 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY galaxyquest.mr.itd.umich.edu ID 477D5397.E161D.20326 ; 
	 3 Jan 2008 16:28:58 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id DEC65ADC79;
	Thu,  3 Jan 2008 21:28:52 +0000 (GMT)
Message-ID: <200801032127.m03LRUqH005177@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 917
          for <source@collab.sakaiproject.org>;
          Thu, 3 Jan 2008 21:28:39 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 1FBB042B30
	for <source@collab.sakaiproject.org>; Thu,  3 Jan 2008 21:28:38 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m03LRUk4005179
	for <source@collab.sakaiproject.org>; Thu, 3 Jan 2008 16:27:30 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m03LRUqH005177
	for source@collab.sakaiproject.org; Thu, 3 Jan 2008 16:27:30 -0500
Date: Thu, 3 Jan 2008 16:27:30 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to cwen@iupui.edu using -f
To: source@collab.sakaiproject.org
From: cwen@iupui.edu
Subject: [sakai] svn commit: r39743 - gradebook/branches/oncourse_2-4-2/app/ui/src/java/org/sakaiproject/tool/gradebook/ui
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Thu Jan  3 16:29:07 2008
X-DSPAM-Confidence: 0.8509
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39743

Author: cwen@iupui.edu
Date: 2008-01-03 16:27:29 -0500 (Thu, 03 Jan 2008)
New Revision: 39743

Modified:
gradebook/branches/oncourse_2-4-2/app/ui/src/java/org/sakaiproject/tool/gradebook/ui/RosterBean.java
Log:
svn merge -c 39403 https://source.sakaiproject.org/svn/gradebook/trunk
U    app/ui/src/java/org/sakaiproject/tool/gradebook/ui/RosterBean.java

svn log -r 39403 https://source.sakaiproject.org/svn/gradebook/trunk
------------------------------------------------------------------------
r39403 | wagnermr@iupui.edu | 2007-12-17 17:11:08 -0500 (Mon, 17 Dec 2007) | 3 lines

SAK-12504
http://jira.sakaiproject.org/jira/browse/SAK-12504
Viewing "All Grades" page as a TA with grader permissions causes stack trace
------------------------------------------------------------------------


----------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences.



From cwen@iupui.edu Thu Jan  3 16:23:48 2008
Return-Path: <postmaster@collab.sakaiproject.org>
Received: from murder (mail.umich.edu [141.211.14.91])
	 by frankenstein.mail.umich.edu (Cyrus v2.3.8) with LMTPA;
	 Thu, 03 Jan 2008 16:23:48 -0500
X-Sieve: CMU Sieve 2.3
Received: from murder ([unix socket])
	 by mail.umich.edu (Cyrus v2.2.12) with LMTPA;
	 Thu, 03 Jan 2008 16:23:48 -0500
Received: from salemslot.mr.itd.umich.edu (salemslot.mr.itd.umich.edu [141.211.14.58])
	by jacknife.mail.umich.edu () with ESMTP id m03LNlf0002115;
	Thu, 3 Jan 2008 16:23:47 -0500
Received: FROM paploo.uhi.ac.uk (app1.prod.collab.uhi.ac.uk [194.35.219.184])
	BY salemslot.mr.itd.umich.edu ID 477D525E.1448.30389 ; 
	 3 Jan 2008 16:23:44 -0500
Received: from paploo.uhi.ac.uk (localhost [127.0.0.1])
	by paploo.uhi.ac.uk (Postfix) with ESMTP id 9D005B9D06;
	Thu,  3 Jan 2008 21:23:38 +0000 (GMT)
Message-ID: <200801032122.m03LMFo4005148@nakamura.uits.iupui.edu>
Mime-Version: 1.0
Content-Transfer-Encoding: 7bit
Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
          by paploo.uhi.ac.uk (JAMES SMTP Server 2.1.3) with SMTP ID 6
          for <source@collab.sakaiproject.org>;
          Thu, 3 Jan 2008 21:23:24 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])
	by shmi.uhi.ac.uk (Postfix) with ESMTP id 3535542B69
	for <source@collab.sakaiproject.org>; Thu,  3 Jan 2008 21:23:24 +0000 (GMT)
Received: from nakamura.uits.iupui.edu (localhost [127.0.0.1])
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11) with ESMTP id m03LMFtT005150
	for <source@collab.sakaiproject.org>; Thu, 3 Jan 2008 16:22:15 -0500
Received: (from apache@localhost)
	by nakamura.uits.iupui.edu (8.12.11.20060308/8.12.11/Submit) id m03LMFo4005148
	for source@collab.sakaiproject.org; Thu, 3 Jan 2008 16:22:15 -0500
Date: Thu, 3 Jan 2008 16:22:15 -0500
X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to cwen@iupui.edu using -f
To: source@collab.sakaiproject.org
From: cwen@iupui.edu
Subject: [sakai] svn commit: r39742 - gradebook/branches/oncourse_2-4-2/app/ui/src/java/org/sakaiproject/tool/gradebook/ui
X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
X-Content-Type-Message-Body: text/plain; charset=UTF-8
Content-Type: text/plain; charset=UTF-8
X-DSPAM-Result: Innocent
X-DSPAM-Processed: Thu Jan  3 16:23:48 2008
X-DSPAM-Confidence: 0.9907
X-DSPAM-Probability: 0.0000

Details: http://source.sakaiproject.org/viewsvn/?view=rev&rev=39742

Author: cwen@iupui.edu
Date: 2008-01-03 16:22:14 -0500 (Thu, 03 Jan 2008)
New Revision: 39742

Modified:
gradebook/branches/oncourse_2-4-2/app/ui/src/java/org/sakaiproject/tool/gradebook/ui/RosterBean.java
Log:
svn merge -c 35014 https://source.sakaiproject.org/svn/gradebook/trunk
U    app/ui/src/java/org/sakaiproject/tool/gradebook/ui/RosterBean.java

svn log -r 35014 https://source.sakaiproject.org/svn/gradebook/trunk
------------------------------------------------------------------------
r35014 | wagnermr@iupui.edu | 2007-09-12 16:17:59 -0400 (Wed, 12 Sep 2007) | 3 lines

SAK-11458
http://bugs.sakaiproject.org/jira/browse/SAK-11458
Course grade does not appear on "All Grades" page if no categories in gb
------------------------------------------------------------------------
This automatic notification message was sent by Sakai Collab (https://collab.sakaiproject.org/portal) from the Source site.
You can modify how you receive notifications at My Workspace > Preferences."""

count= 0
#testing


for line in fh:
    if not line.startswith('From'):
        continue
    if line.startswith('From '):
        continue
    else:
        line = line.split()
        line = line[1]
        print(line)
    count += 1
print("There were",count,"lines in the file with From as the first word")

#not working on visual but in the console in coursera it does 
#must come back to check