<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" indent="yes"/>

    <xsl:template match="/dicts/dict">
        <xsl:copy>
            <xsl:apply-templates select="entry"/>
            <xsl:apply-templates select="document('agfa.xml')/*/entry"/>
            <xsl:apply-templates select="document('fuji.xml')/*/entry"/>
            <xsl:apply-templates select="document('hitachi.xml')/*/entry"/>
            <xsl:apply-templates select="document('gems.xml')/*/entry"/>
            <xsl:apply-templates select="document('pms.xml')/*/entry"/>
            <xsl:apply-templates select="document('siemens.xml')/*/entry"/>
            <xsl:apply-templates select="document('other.xml')/*/entry"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="@* | node()">
        <xsl:copy>
            <xsl:apply-templates select="@* | node()"/>
        </xsl:copy>
    </xsl:template>
</xsl:stylesheet>
