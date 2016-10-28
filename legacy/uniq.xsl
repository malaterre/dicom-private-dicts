<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="xml" indent="yes"/>
  <xsl:key name="entries" match="entry" use="concat(@owner,@group,@element)"/>
  <xsl:template match="/">
    <xsl:comment>
  Program: GDCM (Grassroots DICOM). A DICOM library
  Module:  $URL$

  Copyright (c) 2006-2008 Mathieu Malaterre
  All rights reserved.
  See Copyright.txt or http://gdcm.sourceforge.net/Copyright.html for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notice for more information.
</xsl:comment>
      <dict>
    <xsl:for-each select="//entry[generate-id() = generate-id(key('entries',concat(@owner,@group,@element))[1])]">
      <xsl:sort select="@owner"/>
      <xsl:sort select="@group"/>
      <xsl:sort select="@element"/>
<xsl:element name="entry">
<xsl:copy-of select="@*" /> 
</xsl:element>
    </xsl:for-each>
</dict>
  </xsl:template>
</xsl:stylesheet>
