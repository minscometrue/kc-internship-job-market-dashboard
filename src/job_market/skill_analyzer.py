import pandas as pd


def split_skills(skill_str: str) -> list[str]:
  if pd.isna(skill_str):
    return []

  return [skill.strip() for skill in skill_str.split(";") if skill.strip()]