<?xml version="1.0"?>
<!--
  Copyright (c) 2016 Mathieu Malaterre
-->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:output method="xml"/>
  <xsl:template match="index">
    <dict>
      <xsl:apply-templates/>
    </dict>
  </xsl:template>
  <xsl:template match="file">
    <xsl:apply-templates select="document(string(.))"/>
  </xsl:template>
  <xsl:template name="process-group">
    <xsl:param name="group"/>
    <xsl:value-of select="translate($group,'ABCDEFnyzXYZ','abcdefxxxxxx')"/>
  </xsl:template>
  <xsl:template name="process-element">
    <xsl:param name="element"/>
    <xsl:param name="name" select="''"/>
    <xsl:variable name="lcel">
      <xsl:value-of select="translate($element,'ABCDEFyzXYZ','abcdefxxxxx')"/>
    </xsl:variable>
    <xsl:choose>
      <xsl:when test="string-length($lcel) = 4">
<!-- Need to check if string contains xx in case of LO Private Creator -->
        <xsl:choose>
          <xsl:when test="substring($lcel,1,2) = 'xx'">
            <xsl:value-of select="$lcel"/>
          </xsl:when>
          <xsl:when test="substring($lcel,3,4) = 'xx'">
            <xsl:value-of select="$lcel"/>
          </xsl:when>
          <xsl:otherwise>
<!-- Some cstors use the a value instead of a generic 'xx' notation -->
              <xsl:choose>
            <xsl:when test="substring($lcel,1,2) = '00'">
              <xsl:message>Possible undefined element:<xsl:value-of select="$element"/></xsl:message>
              <xsl:choose>
                <xsl:when test="contains($name,'Private Creator')">
                  <xsl:value-of select="'00xx'"/>
<!-- Of this is a private creator -->
<!-- TODO: check that VR=LO and VM=1 -->
                </xsl:when>
                <xsl:otherwise>
                  <xsl:value-of select="concat('xx',substring($lcel,3,4))"/>
                </xsl:otherwise>
              </xsl:choose>
            </xsl:when>
                <xsl:otherwise>
                  <xsl:value-of select="concat('xx',substring($lcel,3,4))"/>
                </xsl:otherwise>
              </xsl:choose>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <xsl:when test="string-length($lcel) = 2">
        <xsl:value-of select="concat('xx',$lcel)"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:message>UNHANDLED</xsl:message>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <xsl:template name="process-vr">
    <xsl:param name="vr"/>
    <xsl:choose>
      <xsl:when test="$vr = 'AE' or $vr = 'AS' or $vr = 'AT' or $vr = 'CS' or $vr = 'DA' or $vr = 'DS' or $vr = 'DT' or $vr = 'FD' or $vr = 'FL' or $vr = 'IS' or $vr = 'LO' or $vr = 'LT' or $vr = 'OB' or $vr = 'OF' or $vr = 'OW' or $vr = 'PN' or $vr = 'SH' or $vr = 'SL' or $vr = 'SQ' or $vr = 'SS' or $vr = 'ST' or $vr = 'TM' or $vr = 'UI' or $vr = 'UL' or $vr = 'UN' or $vr = 'US' or $vr = 'UT' or $vr = 'OB_OW'">
        <xsl:value-of select="$vr"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:message>Unknown VR:<xsl:value-of select="$vr"/></xsl:message>
        <xsl:value-of select="'UN'"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <xsl:template name="process-vm">
    <xsl:param name="vm"/>
    <xsl:variable name="lcvm">
<!-- I found some GEMS_IDEN_01 / GEMS_PATI_01 ... that use vm=S ... -->
      <xsl:value-of select="translate($vm,'NS','n1')"/>
    </xsl:variable>
    <xsl:choose>
<!-- what should I do when DCS does not specify any VM, should I default to 1 ?? -->
      <xsl:when test="$lcvm = ''">
<!-- SVISION does not have VM -->
        <xsl:value-of select="'1'"/>
      </xsl:when>
<!-- I think they reserve some element but let's just say this is an UN element with vm=1 -->
      <xsl:when test="$lcvm = '0'">
        <xsl:value-of select="'1'"/>
      </xsl:when>
      <xsl:when test="$lcvm = '0-n'">
        <xsl:value-of select="'1-n'"/>
      </xsl:when>
      <xsl:when test="$lcvm = '3n'">
        <xsl:value-of select="'3-n'"/>
      </xsl:when>
      <xsl:when test="$lcvm = 'n'">
        <xsl:value-of select="'1-n'"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:value-of select="$lcvm"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
  <xsl:template name="process-owner">
    <xsl:param name="owner"/>
    <xsl:value-of select="$owner"/>
  </xsl:template>
  <xsl:template name="process-name">
    <xsl:param name="name"/>
    <xsl:value-of select="normalize-space(translate($name,'&gt;',''))"/>
  </xsl:template>
  <xsl:template match="entry">
    <xsl:variable name="current-owner">
      <xsl:choose>
        <xsl:when test="@owner != ''">
          <xsl:value-of select="@owner"/>
        </xsl:when>
        <xsl:when test="../@owner != ''">
          <xsl:value-of select="../@owner"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:value-of select="'UNKNOWN OWNER'"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:variable name="element">
      <xsl:call-template name="process-element">
        <xsl:with-param name="element" select="@element"/>
        <xsl:with-param name="name" select="@name"/>
      </xsl:call-template>
    </xsl:variable>
    <xsl:if test="$element != '00xx'">
<!-- do not add any Private Creator, handled elsewhere -->
      <xsl:element name="entry">
        <xsl:attribute name="owner">
          <xsl:call-template name="process-owner">
            <xsl:with-param name="owner" select="$current-owner"/>
          </xsl:call-template>
        </xsl:attribute>
        <xsl:attribute name="group">
          <xsl:call-template name="process-group">
            <xsl:with-param name="group" select="@group"/>
          </xsl:call-template>
        </xsl:attribute>
        <xsl:attribute name="element">
          <xsl:call-template name="process-element">
            <xsl:with-param name="element" select="@element"/>
          </xsl:call-template>
        </xsl:attribute>
        <xsl:attribute name="vr">
          <xsl:call-template name="process-vr">
            <xsl:with-param name="vr" select="@vr"/>
          </xsl:call-template>
        </xsl:attribute>
        <xsl:attribute name="vm">
          <xsl:call-template name="process-vm">
            <xsl:with-param name="vm" select="@vm"/>
          </xsl:call-template>
        </xsl:attribute>
        <xsl:attribute name="name">
          <xsl:call-template name="process-name">
            <xsl:with-param name="name" select="@name"/>
          </xsl:call-template>
        </xsl:attribute>
      </xsl:element>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
