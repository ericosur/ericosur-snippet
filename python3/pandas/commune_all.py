#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
try:
    import rich.console
    console = rich.console.Console()
    logd = console.log
except ImportError:
    logd = print


class Solution():
    ''' read accumulated commune driving time data and plot boxplot and heatmap
        input: by_dates.csv
        output: boxplot and heatmap
    '''
    alldata_csv = 'by_dates.csv'
    cmap1 = "YlOrRd"
    cmap2 = "coolwarm"

    def __init__(self):
        ''' init '''
        self.df = None
        self.summary = None
        self.__readdata__()

    def __readdata__(self):
        ''' read data '''
        if not os.path.isfile(Solution.alldata_csv):
            logd(f'[FAIL] need data file: {Solution.alldata_csv}')
            logd('[info] use driving_data.py --years --run to generate it')
            sys.exit(1)
        # 假設原始資料有兩欄：date, seconds
        logd(f'[INFO] load data from {self.alldata_csv}')
        self.df = pd.read_csv(Solution.alldata_csv, parse_dates=["date"])
        # I want to print the first row and the last row
        logd(f'[INFO] data loaded, total rows: {len(self.df)}')
        logd(f'[INFO] first row: {self.df.iloc[0].to_dict()}')
        logd(f'[INFO] last row: {self.df.iloc[-1].to_dict()}')
        # 拆分年與月
        self.df["year"] = self.df["date"].dt.year
        self.df["month"] = self.df["date"].dt.month
        # 生成摘要統計 (groupby year, month)
        self.summary = self.df.groupby(["year", "month"])["seconds"].describe(
            percentiles=[0.25, 0.5, 0.75, 0.9, 0.95, 0.99]
        ).reset_index()

    def action(self):
        ''' action '''
        self.plot_box()
        self.plot_heatmap()
        self.deviation_heatmap()

    def plot_box(self):
        ''' boxplot (year x month) '''
        # using raw data to plot boxplot
        plt.figure(figsize=(14,8))
        sns.boxplot(x="month", y="seconds", hue="year", data=self.df)
        plt.title("Commute Time by Year and Month")
        plt.xlabel("Month")
        plt.ylabel("Commute Time (seconds)")
        plt.legend(title="Year")
        plt.show()

    def plot_heatmap(self):
        ''' 熱力圖 (年 × 月) '''
        # 熱力圖：用 median 表示
        pivot_median = self.summary.pivot(index="year", columns="month", values="50%")
        plt.figure(figsize=(12,6))
        sns.heatmap(pivot_median, annot=True, fmt=".0f", cmap=Solution.cmap2, cbar_kws={'label': 'Median Seconds'})
        plt.title("Monthly Median Commute Time (seconds)")
        plt.xlabel("Month")
        plt.ylabel("Year")
        plt.show()

    def deviation_heatmap(self):
        ''' 熱力圖 (年 × 月)，顯示每月中位數相對於長期月均值的偏差百分比 '''
        # 1) done in action()

        # 2) Monthly median per Year×Month
        med = (self.df.groupby(["year","month"])["seconds"]
                .median()
                .rename("MonthlyMedian")
                .reset_index())

        # 3) Long-term monthly average median (climatology by month)
        long_avg = (med.groupby("month")["MonthlyMedian"]
                    .mean()
                    .rename("LongTermMonthlyAvg")
                    .reset_index())

        # 4) Join and compute deviation %
        med = med.merge(long_avg, on="month", how="left")
        med["DeviationPct"] = 100*(med["MonthlyMedian"]-med["LongTermMonthlyAvg"])/med["LongTermMonthlyAvg"]

        # 5) Pivot to Year×Month matrix (ensure full 1..12 columns)
        years  = sorted(med["year"].unique())
        months = list(range(1,13))
        pivot = (med.pivot(index="year", columns="month", values="DeviationPct")
                .reindex(index=years, columns=months))

        # 6) Plot heatmap (matplotlib only)
        fig, ax = plt.subplots(figsize=(12,6))
        im = ax.imshow(pivot.values, aspect="auto", cmap=Solution.cmap2, vmin=np.nanmin(pivot.values), vmax=np.nanmax(pivot.values))
        ax.set_xticks(range(len(months)))
        ax.set_xticklabels(months)
        ax.set_yticks(range(len(years)))
        ax.set_yticklabels(years)
        ax.set_xlabel("Month")
        ax.set_ylabel("Year")
        ax.set_title("Monthly Median Commute Time: Deviation from Long-term Monthly Average (%)")

        # cell annotations
        for i, y in enumerate(years):
            for j, m in enumerate(months):
                v = pivot.iloc[i, j]
                if pd.notna(v):
                    ax.text(j, i, f"{v:.1f}", ha="center", va="center", fontsize=8, color="black")

        # colorbar
        cbar = fig.colorbar(im, ax=ax)
        cbar.set_label("Deviation (%)")

        plt.tight_layout()
        plt.show()
        # plt.savefig(out_png, dpi=200)
        # print(f"Saved: {out_png}")


if __name__ == "__main__":
    sol = Solution()
    sol.action()
