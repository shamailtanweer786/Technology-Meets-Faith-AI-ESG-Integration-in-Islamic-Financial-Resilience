import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# India NPL Ratios (RBI Financial Stability Report 2025) - Your exact table
data = {
    'Period': ['Mar 2025', 'Sep 2025'],
    'Islamic_NPL_pct': [1.8, 1.7],
    'Conventional_NPL_pct': [2.2, 2.1]
}

npl_df = pd.DataFrame(data)

# Convert to decimals for calculations
npl_df['Islamic_NPL'] = npl_df['Islamic_NPL_pct'] / 100
npl_df['Conventional_NPL'] = npl_df['Conventional_NPL_pct'] / 100

# Islamic Advantage (pp)
npl_df['Islamic_Advantage_pct'] = npl_df['Conventional_NPL_pct'] - npl_df['Islamic_NPL_pct']

# Display formatted table (paper-ready)
print("India NPL Ratios (RBI FSR 2025):")
print(npl_df[['Period', 'Islamic_NPL_pct', 'Conventional_NPL_pct', 'Islamic_Advantage_pct']].round(1).to_string(index=False))

# Stats summary
print(f"\n📈 Key Stats:")
print(f"• Average Islamic NPL: {npl_df['Islamic_NPL_pct'].mean():.1f}%")
print(f"• Average Conv NPL: {npl_df['Conventional_NPL_pct'].mean():.1f}%")
print(f"• Consistent Advantage: {npl_df['Islamic_Advantage_pct'].mean():.1f} percentage points")

# Publication-ready visualization (dual panel)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Panel 1: Side-by-side bars
x = np.arange(len(npl_df))
width = 0.35
bars1 = ax1.bar(x - width/2, npl_df['Islamic_NPL_pct'], width, 
                label='Islamic NPL', color='#2E8B57', alpha=0.9, edgecolor='black')
bars2 = ax1.bar(x + width/2, npl_df['Conventional_NPL_pct'], width, 
                label='Conventional NPL', color='#DC143C', alpha=0.9, edgecolor='black')
ax1.set_xlabel('Period')
ax1.set_ylabel('NPL Ratio (%)')
ax1.set_title('RBI FSR 2025: NPL Comparison')
ax1.set_xticks(x)
ax1.set_xticklabels(npl_df['Period'])
ax1.legend()
ax1.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bar in bars1 + bars2:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.05,
             f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')

# Panel 2: Advantage trend
ax2.plot(npl_df['Period'], npl_df['Islamic_Advantage_pct'], 
         marker='o', linewidth=3, markersize=10, color='#4169E1')
ax2.set_ylabel('Islamic Advantage (pp)')
ax2.set_title('Islamic Banking Edge')
ax2.grid(True, alpha=0.3)
ax2.set_ylim(0, max(npl_df['Islamic_Advantage_pct']) * 1.2)

plt.suptitle('India Banking Resilience: Islamic vs Conventional (RBI 2025)', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('RBI_NPL_Analysis_2025.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()

print("\n💾 SAVED: 'RBI_NPL_Analysis_2025.png' (300 DPI - Insert as Figure 3.2 in paper)")
print("✅ Ready for Jamia MSc / Young Economist Competition submission!")
