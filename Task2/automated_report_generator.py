"""
AUTOMATED REPORT GENERATION SCRIPT
Task 2 - Virtual Internship Project
Author: Puneet Chauhan
Date: February 27, 2026
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Image
)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from datetime import datetime
import os


class AutomatedReportGenerator:
    """Main class for automated report generation"""

    def __init__(self, data_file, output_pdf="Sales_Analytics_Report.pdf"):
        self.data_file = data_file
        self.output_pdf = output_pdf
        self.df = None
        self.analysis_results = {}

        # Color scheme
        self.primary_color = HexColor("#2563eb")
        self.secondary_color = HexColor("#10b981")
        self.accent_color = HexColor("#f59e0b")

    def load_data(self):
        """Load and validate data from file"""
        print(f"📂 Loading data from {self.data_file}...")

        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"Data file {self.data_file} not found!")

        # Support CSV and Excel
        if self.data_file.endswith('.csv'):
            self.df = pd.read_csv(self.data_file)
        elif self.data_file.endswith('.xlsx'):
            self.df = pd.read_excel(self.data_file)
        else:
            raise ValueError("Unsupported file format. Use .csv or .xlsx")

        print(f" Data loaded: {len(self.df)} records")
        return self.df

    def analyze_data(self):
        """Perform comprehensive data analysis"""
        print("🔍 Analyzing data...")

        # Convert date column
        self.df['Date'] = pd.to_datetime(self.df['Date'])

        # Overall metrics
        self.analysis_results['total_revenue'] = self.df['Revenue'].sum()
        self.analysis_results['total_quantity'] = self.df['Quantity'].sum()
        self.analysis_results['avg_order_value'] = self.df['Revenue'].mean()
        self.analysis_results['total_transactions'] = len(self.df)

        # Product analysis
        self.analysis_results['product_revenue'] = (
            self.df.groupby('Product')['Revenue']
            .sum()
            .sort_values(ascending=False)
        )
        self.analysis_results['top_product'] = (
            self.analysis_results['product_revenue'].index[0]
        )

        # Region analysis
        self.analysis_results['region_performance'] = (
            self.df.groupby('Region')
            .agg({'Revenue': 'sum', 'Quantity': 'sum'})
            .sort_values('Revenue', ascending=False)
        )
        self.analysis_results['top_region'] = (
            self.analysis_results['region_performance'].index[0]
        )

        # Time series
        self.analysis_results['daily_revenue'] = (
            self.df.groupby('Date')['Revenue'].sum()
        )

        # Customer satisfaction
        self.analysis_results['avg_satisfaction'] = (
            self.df['Customer_Satisfaction'].mean()
        )

        print("Analysis complete")

    def generate_charts(self):
        """Generate visualization charts"""
        print("Generating charts...")

        plt.style.use('seaborn-v0_8-whitegrid')
        sns.set_palette("Set2")

        # Chart 1: Revenue by Product
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        product_rev = self.analysis_results['product_revenue']
        colors = sns.color_palette("viridis", len(product_rev))
        product_rev.plot(kind='barh', ax=ax1, color=colors, edgecolor='black')
        ax1.set_title('Revenue by Product', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Revenue ($)', fontsize=11)
        ax1.set_ylabel('Product', fontsize=11)
        ax1.grid(axis='x', alpha=0.3)
        for i, v in enumerate(product_rev):
            ax1.text(v + 1000, i, f'${v:,.0f}', va='center', fontsize=9)
        plt.tight_layout()
        plt.savefig('chart_product.png', dpi=120, bbox_inches='tight')
        plt.close()

        # Chart 2: Daily Revenue Trend
        fig2, ax2 = plt.subplots(figsize=(8, 4))
        daily_rev = self.analysis_results['daily_revenue']
        ax2.plot(daily_rev.index, daily_rev.values, linewidth=2,
                 color='#2563eb', marker='o', markersize=2)
        ax2.fill_between(daily_rev.index, daily_rev.values,
                         alpha=0.3, color='#3b82f6')
        ax2.set_title('Daily Revenue Trend', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Date', fontsize=11)
        ax2.set_ylabel('Revenue ($)', fontsize=11)
        ax2.grid(alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('chart_trend.png', dpi=120, bbox_inches='tight')
        plt.close()

        # Chart 3: Regional Performance
        fig3, ax3 = plt.subplots(figsize=(8, 4))
        region_data = self.analysis_results['region_performance']
        x = np.arange(len(region_data))
        ax3.bar(x, region_data['Revenue'], color='#10b981', edgecolor='black')
        ax3.set_xlabel('Region', fontsize=11)
        ax3.set_ylabel('Revenue ($)', fontsize=11)
        ax3.set_title('Regional Revenue Performance',
                      fontsize=14, fontweight='bold')
        ax3.set_xticks(x)
        ax3.set_xticklabels(region_data.index)
        ax3.grid(alpha=0.3, axis='y')
        plt.tight_layout()
        plt.savefig('chart_region.png', dpi=120, bbox_inches='tight')
        plt.close()

        print("Charts generated")

    def create_pdf_report(self):
        """Create comprehensive PDF report"""
        print(f"Generating PDF report: {self.output_pdf}...")

        doc = SimpleDocTemplate(
            self.output_pdf,
            pagesize=letter,
            rightMargin=0.75 * inch,
            leftMargin=0.75 * inch,
            topMargin=0.75 * inch,
            bottomMargin=0.75 * inch
        )

        story = []
        styles = getSampleStyleSheet()

        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=self.primary_color,
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        )

        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=16,
            textColor=self.primary_color,
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        )

        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['BodyText'],
            fontSize=11,
            alignment=TA_JUSTIFY,
            spaceAfter=12
        )

        # Title Page
        story.append(Spacer(1, 0.5 * inch))
        story.append(Paragraph("SALES ANALYTICS REPORT", title_style))
        story.append(Spacer(1, 0.2 * inch))

        report_date = datetime.now().strftime("%B %d, %Y")
        story.append(Paragraph(
            f"<b>Report Generated:</b> {report_date}",
            styles['Normal']
        ))
        story.append(Paragraph(
            f"<b>Period:</b> {self.df['Date'].min().strftime('%Y-%m-%d')} to "
            f"{self.df['Date'].max().strftime('%Y-%m-%d')}",
            styles['Normal']
        ))
        story.append(Spacer(1, 0.5 * inch))

        # Executive Summary
        story.append(Paragraph("EXECUTIVE SUMMARY", heading_style))

        summary_text = f"""
        This report provides a comprehensive analysis of sales data covering 
        {len(self.df)} transactions. Total revenue reached 
        <b>${self.analysis_results['total_revenue']:,.2f}</b>, with 
        <b>{self.analysis_results['top_product']}</b> as the top-performing 
        product and <b>{self.analysis_results['top_region']}</b> leading regional sales.
        """
        story.append(Paragraph(summary_text, body_style))
        story.append(Spacer(1, 0.3 * inch))

        # Key Metrics Table
        story.append(Paragraph("KEY PERFORMANCE INDICATORS", heading_style))

        metrics_data = [
            ['Metric', 'Value'],
            ['Total Revenue', f"${self.analysis_results['total_revenue']:,.2f}"],
            ['Total Transactions', f"{self.analysis_results['total_transactions']:,}"],
            ['Total Units Sold', f"{self.analysis_results['total_quantity']:,}"],
            ['Average Order Value', f"${self.analysis_results['avg_order_value']:.2f}"],
            ['Customer Satisfaction', f"{self.analysis_results['avg_satisfaction']:.2f}/5.0"],
            ['Top Product', self.analysis_results['top_product']],
            ['Top Region', self.analysis_results['top_region']]
        ]

        metrics_table = Table(metrics_data, colWidths=[3 * inch, 3 * inch])
        metrics_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), self.primary_color),
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, black),
            ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1),
             [HexColor("#ffffff"), HexColor("#f9fafb")])
        ]))

        story.append(metrics_table)
        story.append(PageBreak())

        # Product Analysis
        story.append(Paragraph("PRODUCT PERFORMANCE ANALYSIS", heading_style))

        if os.path.exists('chart_product.png'):
            img = Image('chart_product.png', width=5.5 * inch, height=3.4 * inch)
            story.append(img)

        story.append(Spacer(1, 0.3 * inch))

        # Revenue Trend
        story.append(Paragraph("REVENUE TREND ANALYSIS", heading_style))

        if os.path.exists('chart_trend.png'):
            img = Image('chart_trend.png', width=5.5 * inch, height=2.75 * inch)
            story.append(img)

        story.append(PageBreak())

        # Regional Analysis
        story.append(Paragraph("REGIONAL PERFORMANCE", heading_style))

        if os.path.exists('chart_region.png'):
            img = Image('chart_region.png', width=5.5 * inch, height=2.75 * inch)
            story.append(img)

        story.append(Spacer(1, 0.5 * inch))

        # Recommendations
        story.append(Paragraph("RECOMMENDATIONS", heading_style))

        recommendations = [
            f"<b>1. Focus on Top Performers:</b> Increase inventory for "
            f"{self.analysis_results['top_product']}.",

            f"<b>2. Regional Strategy:</b> Allocate more resources to "
            f"{self.analysis_results['top_region']} region.",

            f"<b>3. Customer Satisfaction:</b> Improve experience (current: "
            f"{self.analysis_results['avg_satisfaction']:.2f}/5.0).",
        ]

        for rec in recommendations:
            story.append(Paragraph(rec, body_style))
            story.append(Spacer(1, 0.15 * inch))

        # Footer
        story.append(Spacer(1, 0.5 * inch))
        footer_text = f"""
        <para align=center>
        <b>Automated Report System</b><br/>
        CODTECH Virtual Internship - Task 2<br/>
        {datetime.now().strftime("%Y-%m-%d %H:%M")}
        </para>
        """
        story.append(Paragraph(footer_text, styles['Normal']))

        # Build PDF
        doc.build(story)
        print(f"✅ PDF report generated: {self.output_pdf}")

    def generate_report(self):
        """Main method to run complete report generation"""
        print("\n" + "=" * 60)
        print("  AUTOMATED REPORT GENERATION SYSTEM")
        print("=" * 60 + "\n")

        try:
            self.load_data()
            self.analyze_data()
            self.generate_charts()
            self.create_pdf_report()

            print("\n" + "=" * 60)
            print("REPORT GENERATION COMPLETED!")
            print("=" * 60)
            print(f"\nOutput: {self.output_pdf}")
            print(f" Charts: chart_product.png, chart_trend.png, chart_region.png\n")

        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            raise


# Main execution
if __name__ == "__main__":
    generator = AutomatedReportGenerator(
        data_file="sales_data.csv",
        output_pdf="Sales_Analytics_Report.pdf"
    )

    generator.generate_report()
