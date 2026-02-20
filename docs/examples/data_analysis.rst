Data Analysis
=============

Use Case
--------
Analyze Philippine barangay data to gain insights into geographic distributions, demographic patterns, and administrative structures. This is useful for:

* **Market research**: Understand geographic distribution of customers
* **Urban planning**: Analyze barangay density and growth
* **Policy analysis**: Study administrative changes over time
* **Business intelligence**: Make data-driven location decisions
* **Academic research**: Study Philippine geography and demographics

Basic Analysis
--------------

Loading Data into pandas
~~~~~~~~~~~~~~~~~~~~~~~~

Convert barangay data to pandas DataFrames for analysis:

.. code-block:: python

    import pandas as pd
    from barangay import BARANGAY_FLAT

    def load_barangay_dataframe() -> pd.DataFrame:
        """Load barangay data into a pandas DataFrame.

        Returns:
            DataFrame with barangay information
        """
        # Convert flat data to DataFrame
        df = pd.DataFrame(BARANGAY_FLAT)

        # Select relevant columns
        columns = [
            'barangay',
            'province_or_huc',
            'municipality_or_city',
            'psgc_id'
        ]

        # Ensure all columns exist
        available_columns = [col for col in columns if col in df.columns]
        df = df[available_columns]

        return df

    # Example usage
    df = load_barangay_dataframe()
    print(df.head())
    print(f"\nTotal barangays: {len(df)}")

Analyzing Barangay Distributions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Analyze the distribution of barangays across different administrative levels:

.. code-block:: python

    import pandas as pd
    from barangay import BARANGAY_FLAT

    def analyze_barangay_distribution(df: pd.DataFrame) -> dict:
        """Analyze barangay distribution across provinces and municipalities.

        Args:
            df: DataFrame with barangay data

        Returns:
            Dictionary with distribution statistics
        """
        results = {}

        # Barangays per province
        province_counts = df['province_or_huc'].value_counts()
        results['barangays_per_province'] = province_counts

        # Barangays per municipality/city
        municipality_counts = df['municipality_or_city'].value_counts()
        results['barangays_per_municipality'] = municipality_counts

        # Top 10 provinces by barangay count
        results['top_10_provinces'] = province_counts.head(10)

        # Summary statistics
        results['summary'] = {
            'total_barangays': len(df),
            'total_provinces': df['province_or_huc'].nunique(),
            'total_municipalities': df['municipality_or_city'].nunique(),
            'avg_barangays_per_province': province_counts.mean(),
            'max_barangays_in_province': province_counts.max(),
            'min_barangays_in_province': province_counts.min()
        }

        return results

    # Example usage
    df = load_barangay_dataframe()
    analysis = analyze_barangay_distribution(df)

    print("Summary Statistics:")
    for key, value in analysis['summary'].items():
        print(f"  {key}: {value}")

    print("\nTop 10 Provinces by Barangay Count:")
    print(analysis['top_10_provinces'])

Statistical Analysis by Region
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Perform statistical analysis grouped by region or province:

.. code-block:: python

    import pandas as pd
    from barangay import BARANGAY_FLAT

    def analyze_by_province(df: pd.DataFrame) -> pd.DataFrame:
        """Analyze barangay statistics by province.

        Args:
            df: DataFrame with barangay data

        Returns:
            DataFrame with statistics by province
        """
        # Group by province and calculate statistics
        stats = df.groupby('province_or_huc').agg({
            'barangay': ['count', 'nunique'],
            'municipality_or_city': 'nunique'
        }).reset_index()

        # Flatten multi-level columns
        stats.columns = [
            'province',
            'total_barangays',
            'unique_barangays',
            'unique_municipalities'
        ]

        # Sort by total barangays
        stats = stats.sort_values('total_barangays', ascending=False)

        return stats

    # Example usage
    df = load_barangay_dataframe()
    stats = analyze_by_province(df)
    print(stats.head(10))

Data Visualization
------------------

Visualizing Barangay Distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create visualizations to understand barangay distributions:

.. code-block:: python

    import pandas as pd
    import matplotlib.pyplot as plt
    from barangay import BARANGAY_FLAT

    def plot_barangay_distribution(
        df: pd.DataFrame,
        top_n: int = 15,
        figsize: tuple = (12, 6)
    ) -> None:
        """Plot barangay distribution by province.

        Args:
            df: DataFrame with barangay data
            top_n: Number of top provinces to display
            figsize: Figure size
        """
        # Get top N provinces by barangay count
        top_provinces = df['province_or_huc'].value_counts().head(top_n)

        # Create bar plot
        fig, ax = plt.subplots(figsize=figsize)
        top_provinces.plot(kind='bar', ax=ax, color='steelblue')

        ax.set_xlabel('Province', fontsize=12)
        ax.set_ylabel('Number of Barangays', fontsize=12)
        ax.set_title(f'Top {top_n} Provinces by Barangay Count', fontsize=14, fontweight='bold')
        ax.tick_params(axis='x', rotation=45, labelsize=10)
        ax.tick_params(axis='y', labelsize=10)

        plt.tight_layout()
        plt.show()

    # Example usage
    df = load_barangay_dataframe()
    plot_barangay_distribution(df, top_n=15)

Visualizing Municipalities per Province
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a heatmap or stacked bar chart:

.. code-block:: python

    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    def plot_municipality_heatmap(
        df: pd.DataFrame,
        top_provinces: int = 10,
        figsize: tuple = (14, 8)
    ) -> None:
        """Plot heatmap of barangays per municipality for top provinces.

        Args:
            df: DataFrame with barangay data
            top_provinces: Number of top provinces to display
            figsize: Figure size
        """
        # Get top N provinces
        top_provs = df['province_or_huc'].value_counts().head(top_provinces).index

        # Filter data for top provinces
        filtered_df = df[df['province_or_huc'].isin(top_provs)]

        # Create pivot table
        pivot_table = filtered_df.pivot_table(
            index='province_or_huc',
            columns='municipality_or_city',
            values='barangay',
            aggfunc='count',
            fill_value=0
        )

        # For better visualization, limit municipalities
        top_municipalities = pivot_table.sum().sort_values(ascending=False).head(20).index
        pivot_table = pivot_table[top_municipalities]

        # Create heatmap
        fig, ax = plt.subplots(figsize=figsize)
        sns.heatmap(
            pivot_table,
            cmap='YlOrRd',
            ax=ax,
            cbar_kws={'label': 'Number of Barangays'}
        )

        ax.set_xlabel('Municipality/City', fontsize=12)
        ax.set_ylabel('Province', fontsize=12)
        ax.set_title('Barangay Distribution Heatmap', fontsize=14, fontweight='bold')

        plt.tight_layout()
        plt.show()

    # Example usage
    df = load_barangay_dataframe()
    plot_municipality_heatmap(df, top_provinces=10)

Working with Historical Data
----------------------------

Analyzing Administrative Changes Over Time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compare barangay data across different dates to track changes:

.. code-block:: python

    import pandas as pd
    from barangay import load_barangay_flat_data
    from barangay.date_resolver import get_available_dates

    def compare_historical_data(
        date1: str,
        date2: str
    ) -> dict:
        """Compare barangay data between two dates.

        Args:
            date1: First date (YYYY-MM-DD)
            date2: Second date (YYYY-MM-DD)

        Returns:
            Dictionary with comparison results
        """
        # Load data for both dates
        data1 = load_barangay_flat_data(as_of=date1)
        data2 = load_barangay_flat_data(as_of=date2)

        # Convert to DataFrames
        df1 = pd.DataFrame(data1)
        df2 = pd.DataFrame(data2)

        # Get PSGC IDs for comparison
        psgc_ids_1 = set(df1['psgc_id'].unique())
        psgc_ids_2 = set(df2['psgc_id'].unique())

        # Find differences
        added = psgc_ids_2 - psgc_ids_1
        removed = psgc_ids_1 - psgc_ids_2
        common = psgc_ids_1 & psgc_ids_2

        # Get details of changes
        added_barangays = df2[df2['psgc_id'].isin(added)]
        removed_barangays = df1[df1['psgc_id'].isin(removed)]

        return {
            'date1': date1,
            'date2': date2,
            'total_barangays_date1': len(df1),
            'total_barangays_date2': len(df2),
            'barangays_added': len(added),
            'barangays_removed': len(removed),
            'barangays_unchanged': len(common),
            'added_details': added_barangays,
            'removed_details': removed_barangays
        }

    # Example usage
    available = get_available_dates()
    if len(available) >= 2:
        comparison = compare_historical_data(available[0], available[1])
        print(f"Comparison between {comparison['date1']} and {comparison['date2']}:")
        print(f"  Barangays added: {comparison['barangays_added']}")
        print(f"  Barangays removed: {comparison['barangays_removed']}")
        print(f"  Barangays unchanged: {comparison['barangays_unchanged']}")

Time Series Analysis of Barangay Growth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Analyze barangay growth over multiple data releases:

.. code-block:: python

    import pandas as pd
    from barangay import load_barangay_flat_data
    from barangay.date_resolver import get_available_dates

    def analyze_barangay_growth() -> pd.DataFrame:
        """Analyze barangay growth over time.

        Returns:
            DataFrame with growth statistics by date
        """
        dates = get_available_dates()
        results = []

        for date in dates:
            data = load_barangay_flat_data(as_of=date)
            df = pd.DataFrame(data)

            results.append({
                'date': date,
                'total_barangays': len(df),
                'total_provinces': df['province_or_huc'].nunique(),
                'total_municipalities': df['municipality_or_city'].nunique()
            })

        return pd.DataFrame(results).sort_values('date')

    # Example usage
    growth_df = analyze_barangay_growth()
    print(growth_df)

    # Plot growth
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(growth_df['date'], growth_df['total_barangays'], marker='o', linewidth=2)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Total Barangays', fontsize=12)
    ax.set_title('Barangay Growth Over Time', fontsize=14, fontweight='bold')
    ax.tick_params(axis='x', rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

Complete BarangayDataAnalyzer Class
-----------------------------------

Here's a comprehensive BarangayDataAnalyzer class for various analyses:

.. code-block:: python

    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from typing import Optional, Dict, Any, List
    from barangay import BARANGAY_FLAT, load_barangay_flat_data
    from barangay.date_resolver import get_available_dates

    class BarangayDataAnalyzer:
        """Comprehensive analyzer for Philippine barangay data.

        This class provides methods for analyzing barangay distributions,
        performing statistical analysis, creating visualizations, and
        tracking changes over time.

        Attributes:
            df: DataFrame with barangay data
            data_date: Date of the data being analyzed
        """

        def __init__(self, data: Optional[pd.DataFrame] = None, as_of: Optional[str] = None):
            """Initialize the BarangayDataAnalyzer.

            Args:
                data: Optional DataFrame with barangay data
                as_of: Optional date string (YYYY-MM-DD) for historical data
            """
            if data is not None:
                self.df = data
                self.data_date = 'custom'
            else:
                flat_data = load_barangay_flat_data(as_of=as_of)
                self.df = pd.DataFrame(flat_data)
                self.data_date = as_of if as_of else 'current'

        def load_dataframe(self) -> pd.DataFrame:
            """Get the barangay DataFrame.

            Returns:
                DataFrame with barangay data
            """
            return self.df.copy()

        def get_summary_statistics(self) -> Dict[str, Any]:
            """Get summary statistics of the barangay data.

            Returns:
                Dictionary with summary statistics
            """
            return {
                'data_date': self.data_date,
                'total_barangays': len(self.df),
                'total_provinces': self.df['province_or_huc'].nunique(),
                'total_municipalities': self.df['municipality_or_city'].nunique(),
                'avg_barangays_per_province': self.df.groupby('province_or_huc').size().mean(),
                'max_barangays_in_province': self.df.groupby('province_or_huc').size().max(),
                'min_barangays_in_province': self.df.groupby('province_or_huc').size().min()
            }

        def analyze_by_province(self) -> pd.DataFrame:
            """Analyze barangay statistics by province.

            Returns:
                DataFrame with statistics by province
            """
            stats = self.df.groupby('province_or_huc').agg({
                'barangay': ['count', 'nunique'],
                'municipality_or_city': 'nunique'
            }).reset_index()

            stats.columns = [
                'province',
                'total_barangays',
                'unique_barangays',
                'unique_municipalities'
            ]

            return stats.sort_values('total_barangays', ascending=False)

        def analyze_by_municipality(self) -> pd.DataFrame:
            """Analyze barangay statistics by municipality.

            Returns:
                DataFrame with statistics by municipality
            """
            stats = self.df.groupby(['province_or_huc', 'municipality_or_city']).agg({
                'barangay': ['count', 'nunique']
            }).reset_index()

            stats.columns = [
                'province',
                'municipality',
                'total_barangays',
                'unique_barangays'
            ]

            return stats.sort_values('total_barangays', ascending=False)

        def get_top_provinces(self, n: int = 10) -> pd.DataFrame:
            """Get top N provinces by barangay count.

            Args:
                n: Number of top provinces to return

            Returns:
                DataFrame with top N provinces
            """
            province_counts = self.df['province_or_huc'].value_counts().head(n)
            return pd.DataFrame({
                'province': province_counts.index,
                'barangay_count': province_counts.values
            })

        def get_top_municipalities(self, n: int = 10) -> pd.DataFrame:
            """Get top N municipalities by barangay count.

            Args:
                n: Number of top municipalities to return

            Returns:
                DataFrame with top N municipalities
            """
            municipality_counts = self.df['municipality_or_city'].value_counts().head(n)
            return pd.DataFrame({
                'municipality': municipality_counts.index,
                'barangay_count': municipality_counts.values
            })

        def filter_by_province(self, province: str) -> pd.DataFrame:
            """Filter barangay data by province.

            Args:
                province: Province name to filter by

            Returns:
                Filtered DataFrame
            """
            return self.df[self.df['province_or_huc'] == province].copy()

        def filter_by_municipality(self, municipality: str) -> pd.DataFrame:
            """Filter barangay data by municipality.

            Args:
                municipality: Municipality name to filter by

            Returns:
                Filtered DataFrame
            """
            return self.df[self.df['municipality_or_city'] == municipality].copy()

        def plot_province_distribution(
            self,
            top_n: int = 15,
            figsize: tuple = (12, 6),
            save_path: Optional[str] = None
        ) -> None:
            """Plot barangay distribution by province.

            Args:
                top_n: Number of top provinces to display
                figsize: Figure size
                save_path: Optional path to save the plot
            """
            top_provinces = self.df['province_or_huc'].value_counts().head(top_n)

            fig, ax = plt.subplots(figsize=figsize)
            top_provinces.plot(kind='bar', ax=ax, color='steelblue')

            ax.set_xlabel('Province', fontsize=12)
            ax.set_ylabel('Number of Barangays', fontsize=12)
            ax.set_title(f'Top {top_n} Provinces by Barangay Count', fontsize=14, fontweight='bold')
            ax.tick_params(axis='x', rotation=45, labelsize=10)
            ax.tick_params(axis='y', labelsize=10)

            plt.tight_layout()

            if save_path:
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.show()

        def plot_municipality_distribution(
            self,
            province: Optional[str] = None,
            top_n: int = 15,
            figsize: tuple = (12, 6),
            save_path: Optional[str] = None
        ) -> None:
            """Plot barangay distribution by municipality.

            Args:
                province: Optional province to filter by
                top_n: Number of top municipalities to display
                figsize: Figure size
                save_path: Optional path to save the plot
            """
            if province:
                df = self.filter_by_province(province)
                title = f'Top {top_n} Municipalities in {province}'
            else:
                df = self.df
                title = f'Top {top_n} Municipalities by Barangay Count'

            top_municipalities = df['municipality_or_city'].value_counts().head(top_n)

            fig, ax = plt.subplots(figsize=figsize)
            top_municipalities.plot(kind='bar', ax=ax, color='coral')

            ax.set_xlabel('Municipality/City', fontsize=12)
            ax.set_ylabel('Number of Barangays', fontsize=12)
            ax.set_title(title, fontsize=14, fontweight='bold')
            ax.tick_params(axis='x', rotation=45, labelsize=10)
            ax.tick_params(axis='y', labelsize=10)

            plt.tight_layout()

            if save_path:
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.show()

        def export_report(
            self,
            output_path: str,
            format: str = 'excel',
            include_plots: bool = False
        ) -> None:
            """Export analysis report to file.

            Args:
                output_path: Path to output file
                format: Output format ('excel' or 'csv')
                include_plots: Whether to include plots (for Excel)
            """
            if format == 'csv':
                self.df.to_csv(output_path, index=False)
            elif format == 'excel':
                with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
                    # Summary
                    summary_df = pd.DataFrame([self.get_summary_statistics()])
                    summary_df.to_excel(writer, sheet_name='Summary', index=False)

                    # Province analysis
                    province_stats = self.analyze_by_province()
                    province_stats.to_excel(writer, sheet_name='By Province', index=False)

                    # Municipality analysis
                    municipality_stats = self.analyze_by_municipality()
                    municipality_stats.to_excel(writer, sheet_name='By Municipality', index=False)

                    # Raw data
                    self.df.to_excel(writer, sheet_name='Raw Data', index=False)
            else:
                raise ValueError(f"Unsupported format: {format}")

    # Example usage
    if __name__ == '__main__':
        # Initialize analyzer
        analyzer = BarangayDataAnalyzer()

        # Get summary statistics
        summary = analyzer.get_summary_statistics()
        print("Summary Statistics:")
        for key, value in summary.items():
            print(f"  {key}: {value}")

        # Get top provinces
        top_provinces = analyzer.get_top_provinces(n=10)
        print("\nTop 10 Provinces:")
        print(top_provinces)

        # Analyze by province
        province_stats = analyzer.analyze_by_province()
        print("\nProvince Statistics:")
        print(province_stats.head())

        # Filter by province
        manila_data = analyzer.filter_by_province('National Capital Region (NCR)')
        print(f"\nBarangays in NCR: {len(manila_data)}")

        # Plot distributions
        analyzer.plot_province_distribution(top_n=15)
        analyzer.plot_municipality_distribution(province='National Capital Region (NCR)', top_n=10)

        # Export report
        analyzer.export_report('barangay_analysis_report.xlsx', format='excel')

Exporting and Reporting
-----------------------

Creating Comprehensive Reports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generate detailed reports with multiple sections:

.. code-block:: python

    import pandas as pd
    from barangay import BARANGAY_FLAT

    def generate_comprehensive_report(output_path: str) -> None:
        """Generate a comprehensive barangay analysis report.

        Args:
            output_path: Path to save the Excel report
        """
        df = pd.DataFrame(BARANGAY_FLAT)

        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            # Executive Summary
            summary = {
                'Metric': [
                    'Total Barangays',
                    'Total Provinces',
                    'Total Municipalities/Cities',
                    'Avg Barangays per Province',
                    'Max Barangays in Province',
                    'Min Barangays in Province'
                ],
                'Value': [
                    len(df),
                    df['province_or_huc'].nunique(),
                    df['municipality_or_city'].nunique(),
                    df.groupby('province_or_huc').size().mean(),
                    df.groupby('province_or_huc').size().max(),
                    df.groupby('province_or_huc').size().min()
                ]
            }
            pd.DataFrame(summary).to_excel(writer, sheet_name='Executive Summary', index=False)

            # Top 20 Provinces
            top_provinces = df['province_or_huc'].value_counts().head(20)
            pd.DataFrame({
                'Province': top_provinces.index,
                'Barangay Count': top_provinces.values
            }).to_excel(writer, sheet_name='Top Provinces', index=False)

            # Top 20 Municipalities
            top_municipalities = df['municipality_or_city'].value_counts().head(20)
            pd.DataFrame({
                'Municipality': top_municipalities.index,
                'Barangay Count': top_municipalities.values
            }).to_excel(writer, sheet_name='Top Municipalities', index=False)

            # Province Statistics
            province_stats = df.groupby('province_or_huc').agg({
                'barangay': 'count',
                'municipality_or_city': 'nunique'
            }).reset_index()
            province_stats.columns = ['Province', 'Barangay Count', 'Municipality Count']
            province_stats = province_stats.sort_values('Barangay Count', ascending=False)
            province_stats.to_excel(writer, sheet_name='Province Statistics', index=False)

            # Raw Data (first 1000 rows for preview)
            df.head(1000).to_excel(writer, sheet_name='Data Preview', index=False)

    # Example usage
    generate_comprehensive_report('barangay_comprehensive_report.xlsx')

Performance Tips
----------------

1. **Use appropriate data types**: Convert string columns to categorical for better performance:

.. code-block:: python

    df['province_or_huc'] = df['province_or_huc'].astype('category')
    df['municipality_or_city'] = df['municipality_or_city'].astype('category')

2. **Filter early**: Apply filters before aggregating to reduce computation:

.. code-block:: python

    # Instead of aggregating all data then filtering
    df_filtered = df[df['province_or_huc'] == 'National Capital Region (NCR)']
    stats = df_filtered.groupby('municipality_or_city').size()

3. **Use vectorized operations**: Avoid loops when possible:

.. code-block:: python

    # Good - vectorized
    df['is_ncr'] = df['province_or_huc'] == 'National Capital Region (NCR)'

    # Avoid - loop
    # for idx, row in df.iterrows():
    #     df.at[idx, 'is_ncr'] = row['province_or_huc'] == 'National Capital Region (NCR)'

4. **Cache computations**: Store intermediate results if used multiple times:

.. code-block:: python

    class CachedAnalyzer(BarangayDataAnalyzer):
        """Analyzer with caching."""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._cache = {}

        def analyze_by_province(self):
            """Analyze by province with caching."""
            if 'province_stats' not in self._cache:
                self._cache['province_stats'] = super().analyze_by_province()
            return self._cache['province_stats'].copy()

See Also
--------

* :ref:`api-data` - Data loading API reference
* :ref:`userguide-data-models` - Data models user guide
* :ref:`examples-batch-processing` - Batch processing examples
* :ref:`advanced-caching` - Caching mechanisms