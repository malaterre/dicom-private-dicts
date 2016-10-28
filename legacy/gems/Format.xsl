<?xml version="1.0" encoding="UTF-8"?>
<!--
  Program: GDCM (Grassroots DICOM). A DICOM library
  Module:  $URL$

  Copyright (c) 2006-2008 Mathieu Malaterre
  All rights reserved.
  See Copyright.txt or http://gdcm.sourceforge.net/Copyright.html for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notice for more information.
-->
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
xmlns:xs="http://www.w3.org/2001/XMLSchema"
xmlns:gdcm="http://sf.net/gdcm">

<xsl:function name="gdcm:cleanup" as="xs:string*">
  <xsl:param name="s" as="xs:string*"/>
  <xsl:sequence select="normalize-space(translate($s,'>',''))"/>
</xsl:function>

<xsl:function name="gdcm:get-vm" as="xs:string*">
  <xsl:param name="vm" as="xs:string*"/>
  <xsl:variable name="s" select="lower-case($vm)"/>
  <xsl:sequence select="translate($s,'s','1')"/>
</xsl:function>

<xsl:template name="format-element">
  <xsl:param name="entry"/>
  <xsl:variable name="element" select="lower-case($entry/@element)"/>
  <xsl:variable name="l" select="string-length($element)"/>
  <xsl:variable name="element02" select="substring($element,number($l)-3,number($l)-2)"/>
  <xsl:variable name="element24" select="substring($element,number($l)-1,number($l))"/>
    <xsl:choose>
	    <xsl:when test="($element02 = '00' and $element24 = 'xx') or $element='0010' or $element = 'xxxx' ">
		    <!-- Need to check VR=LO and VM=1 ?? -->
		    <!-- Need to check name=Private.* ?? -->
        <xsl:value-of select="'00xx'"/>
	    </xsl:when>
	    <xsl:when test="$l = 2 or $element02 = 'xx' or $element02 = '00' or $element02 = '10'"> <!-- some cstor actually use 00/10 instead of xx -->
		    <xsl:text>xx</xsl:text><xsl:value-of select="lower-case($element24)"/>
	    </xsl:when>
      <xsl:otherwise>
	      <xsl:message>error: 
		      <xsl:value-of select="$entry"/>
		      <xsl:value-of select="$entry/@group"/>
		      <xsl:value-of select="$element"/>
	      </xsl:message>
      </xsl:otherwise>
    </xsl:choose>
</xsl:template>

<xsl:function name="gdcm:format-element" as="xs:string*">
  <xsl:param name="g" as="xs:string*"/>
  <xsl:param name="e" as="xs:string*"/>
  <xsl:variable name="s-length" select="string-length($e)"/>
        <!--xsl:if test="position() != last()"-->
  <xsl:sequence select="substring($e,3,4)"/>
</xsl:function>

  <xsl:template match="entry">
          <xsl:variable name="group" select="lower-case(@group)"/>
          <xsl:variable name="element" >
        <xsl:call-template name="format-element">
          <xsl:with-param name="entry" select="."/>
	</xsl:call-template>
	  </xsl:variable>
          <xsl:variable name="vr" select="@vr"/>
          <xsl:variable name="vm" select="gdcm:get-vm(@vm)"/>
          <xsl:variable name="owner" select="@owner"/>
          <xsl:variable name="owner-parent" select="../@owner"/> <!-- get parent owner -->
          <xsl:variable name="name" select="gdcm:cleanup(@name)"/> <!-- get parent owner -->
	  <entry owner="{normalize-space(($owner,$owner-parent))}" group="{$group}" element="{$element}" vr="{$vr}" vm="{$vm}" name="{$name}"/>
  </xsl:template>

  <xsl:template match="dict">
    <xsl:apply-templates/>
  </xsl:template>

  <xsl:template match="dicts">
  <xsl:apply-templates/>
  </xsl:template>

  <xsl:template match="/">
  <dict>
    <xsl:apply-templates/>
  </dict>
  </xsl:template>


</xsl:stylesheet>
