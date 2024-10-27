select player_name,gender,score_points, sum(score_points)
  OVER (Partition by gender order by day Rows between unbounded preceding and current row)
  as cumulative_score 
  from players_scores 
  order by gender , day;
