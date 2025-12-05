import random


def single_game(player1_name, player2_name, player1_win_rate=0.5):
    """
    模拟单局比赛
    :param player1_name: 选手1名称
    :param player2_name: 选手2名称
    :param player1_win_rate: 选手1每球获胜概率（0-1之间）
    :return: 选手1得分，选手2得分
    """
    player1_score = 0
    player2_score = 0
    server = 1  # 1表示player1发球，2表示player2发球
    serve_count = 0  # 每轮发球次数计数

    while True:
        # 根据胜率模拟得分
        if random.random() < player1_win_rate:
            # 选手1得分
            if server == 1:
                player1_score += 1
            else:
                player1_score += 1
        else:
            # 选手2得分
            if server == 2:
                player2_score += 1
            else:
                player2_score += 1

        # 检查获胜条件：至少11分且领先2分
        if (max(player1_score, player2_score) >= 11 and
                abs(player1_score - player2_score) >= 2):
            break

        # 发球次数管理：每发2球切换发球方
        serve_count += 1
        if serve_count >= 2:
            server = 2 if server == 1 else 1
            serve_count = 0

    return player1_score, player2_score


def ping_pong_match():
    """完整比赛（多局）"""
    # 获取选手信息
    print("=== 乒乓球比赛模拟器 ===")
    player1_name = input("请输入选手A的名字：").strip() or "选手A"
    player2_name = input("请输入选手B的名字：").strip() or "选手B"

    # 获取选手胜率
    while True:
        try:
            player1_win_rate = float(input(f"\n请输入{player1_name}的每球获胜概率（0-1之间，例如0.5）："))
            if 0 <= player1_win_rate <= 1:
                player2_win_rate = 1 - player1_win_rate
                break
            else:
                print("请输入0到1之间的数值！")
        except ValueError:
            print("请输入有效的数字！")

    # 获取比赛规则
    while True:
        try:
            print("\n请选择比赛规则：")
            print("1. 一局定胜负")
            print("2. 三局两胜")
            print("3. 五局三胜")
            print("4. 七局四胜")
            choice = int(input("请输入选项（1-4）："))

            if choice == 1:
                total_games = 1
                win_needed = 1
                break
            elif choice == 2:
                total_games = 3
                win_needed = 2
                break
            elif choice == 3:
                total_games = 5
                win_needed = 3
                break
            elif choice == 4:
                total_games = 7
                win_needed = 4
                break
            else:
                print("请输入1-4之间的数字！")
        except ValueError:
            print("请输入有效的数字！")

    print(f"\n=== 开始{total_games}局{win_needed}胜的比赛 ===")
    print(f"{player1_name}（胜率：{player1_win_rate:.1%}）VS {player2_name}（胜率：{player2_win_rate:.1%}）")
    print("-" * 60)

    player1_wins = 0
    player2_wins = 0
    game_num = 1

    # 进行比赛直到一方达到获胜所需局数
    while player1_wins < win_needed and player2_wins < win_needed:
        print(f"\n第{game_num}局比赛开始：")
        score1, score2 = single_game(player1_name, player2_name, player1_win_rate)

        # 记录本局结果
        if score1 > score2:
            player1_wins += 1
            round_winner = player1_name
        else:
            player2_wins += 1
            round_winner = player2_name

        print(f"第{game_num}局结束，{round_winner}获胜，比分：{score1} : {score2}")
        print(f"目前总战绩：{player1_name} {player1_wins} - {player2_wins} {player2_name}")
        print("-" * 60)

        game_num += 1

    # 最终结果
    final_winner = player1_name if player1_wins > player2_wins else player2_name
    print(f"\n🎉 比赛最终结果：{final_winner}以{max(player1_wins, player2_wins)}:{min(player1_wins, player2_wins)}获胜！")

    # 显示统计信息
    print(f"\n=== 比赛统计 ===")
    print(f"{player1_name} 获胜局数：{player1_wins}")
    print(f"{player2_name} 获胜局数：{player2_wins}")
    print(f"胜率设置：{player1_name} {player1_win_rate:.1%} / {player2_name} {player2_win_rate:.1%}")


if __name__ == "__main__":
    ping_pong_match()
