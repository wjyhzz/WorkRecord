死斗网站：https://tgpro.net/

https://csgo.moeub.cn/server

https://next.moeub.cn/cs2



// ====== 基本调试与作弊设置 ======

```
sv_cheats true                      // 开启作弊模式
sv_showimpacts 1                    // 显示击中效果
sv_grenade_trajectory_prac_preview 1 // 启用投掷点预览
sv_grenade_trajectory_prac_tracaltime 8 // 轨迹线显示时长：8 秒
sv_grenade_trajectory_time_spectator 4 // 投掷物轨迹时长：4 秒
buddha true                         // 开启buddha模式
buddha_reset_hp 100                 // 每次0血后重置为 100 生命值
sv_infinite_ammo 1                  // 无限弹药
endround                            // 结束当前回合
mp_restartgame 1                    // 重启当前回合
```

// ====== 回合与队伍控制 ======

```
mp_ignore_round_win_conditions 1   // 忽略回合胜利条件（保证一直可跑图）
mp_round_restart_delay 0           // 回合重延迟为：0
mp_roundtime 60                    // 普通回合时间：60 秒
mp_roundtime_defuse 60             // 拆弹模式回合时间：60 秒
mp_roundtime_hostage 60            // 人质模式回合时间：60 秒
mp_freezetime 0                    // 回合准备时间：0
cl_versus_intro_time 0             // 关闭比赛开场动画
mp_team_intro 0                    // 关闭队伍介绍时间
```

// ====== 死亡后重生设置 ======

```
mp_respawn_on_death_ct 1           // CT 死亡后自动重生
mp_respawn_on_death_t 1            // T 死亡后自动重生
mp_respawnwavetime_ct 1            // CT 重生波间隔 1 秒
mp_respawnwavetime_t 1             // T 重生波间隔 1 秒
mp_respawn_immunitytime 0          // 重生无敌时间：0 秒
```

// ====== Bot 管理 ======

```
bot_kick                           // 踢出所有 Bot
bot_stop 1                         // 停止 Bot 行动
```

// ====== 武器与投掷物设置 ======

```
ammo_grenade_limit_total 99999     // 投掷物最大携带数量：无限
mp_death_drop_grenade 0            // 死亡不掉落投掷物
mp_drop_knife_enable 1             // 允许丢弃刀具
```

// ====== 经济系统调整 ======

```
mp_maxmoney 99999                  // 最大金钱：99999
mp_startmoney 99999                // 起始金钱：99999
mp_buy_anywhere 1                  // 全地图购买
mp_buytime 99999                   // 无限购买时间
mp_free_armor 2                    // 默认拥有全甲
mp_defuser_allocation 2            // CT 默认有拆弹器
```

// ====== 渲染与视图 ======

```
r_draw_instances 0                // 关闭实例化渲染
```

// ====== 趣味性设置 ======

```
mp_teamname_1 "❤️"                 // 队伍1名称
mp_teamname_2 "❤️"                 // 队伍2名称
mp_anyone_can_pickup_c4 true      // 任意人可拾取 c4
```

