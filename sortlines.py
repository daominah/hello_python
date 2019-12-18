def sortLines(s: str) -> str:
    lines = s.split('\n')
    lines.sort()
    ret = '\n'.join(lines)
    print(ret)

sortLines("""
	  code;
      refCode;
      description;
      descriptionEn;
      market;
      lastTradingDate;
      open;
      high;
      low;
      last;
      change;
      rate;
      tradingVolume;
      tradingValue;
      priorTradingVolume;
      upCount;
      ceilingCount;
      downCount;
      floorCount;
      unchangedCount;
      isHighlight;
      createdAt;""")
