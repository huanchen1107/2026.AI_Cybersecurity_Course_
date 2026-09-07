# AIIS_L2 — Content-Driven Visual Audit（S01–S30）

Date: 2026-09-07
Status: PASS WITH VISUAL ENHANCEMENTS
Purpose: 逐頁確認 L2 的 Visual 與「煥哥」由當頁工程概念驅動，而不是人物裝飾。

## Audit Standard
Concept → Visual Metaphor → Huange Role → Expression → Action → Prop → Content Interaction → Placement.

## S01–S06 — Vibe Coding → Spec-Driven Engineering
- S01 Working ≠ Managed — ENHANCE. Project Lead 不只左右指；應站在 WORKING 與四個管理問號之間的未完成橋樑上，手上拿 `CHANGE` 卡，視覺化「功能完成後開始管理變更」。
- S02 Change Surface — PASS. 小 Request 在手中、背後展開 UI/Backend/Data/Dependency cards；人物回頭驚訝看擴散面。
- S03 Fast Creation → Controlled Evolution — ENHANCE. 同一煥哥左右時間狀態：左側 Vibe Builder 衝刺完成；右側 Engineering Lead 面對 Change #1–#10 timeline，用 history board 追蹤，不只是換表情。
- S04 Prompt vs Spec — PASS. 左手 transient chat bubble、右手 persistent structured Spec card；兩者不是敵對而是不同角色。
- S05 OpenSpec — PASS. Change Owner 親手把漂浮 User Request 放入 Repository 中的 OpenSpec Change folder，突出「從 Chat 搬進 Project」。
- S06 Four Layers — ENHANCE. Engineering Lead 應站在 DEFINE→BUILD→VERIFY→REMEMBER 上方 Human control rail，分別用手勢指四站；人物不是只站著介紹工具名稱。

## S07–S12 — DEFINE
- S07 Problem→Need→Change — PASS. Product Owner 面向使用者，先聽問題，再把 Need card 放入 Change；不碰 Code。
- S08 Change Unit — PASS. Change Manager 把 WHY/SCOPE/REQ/DONE 零散卡片收進同一 Change Folder。
- S09 WHY — ENHANCE. Requirement Investigator 用 WHY magnifier 擋在 AI→HOW shortcut 前，將 `Add div` 卡退回，保留 `Users need freshness visibility`。
- S10 Scope — PASS. Scope Gatekeeper 實際放行 Last Updated cards、擋住 Auth/DB redesign/Framework refactor；Scope Creep 可做小怪獸但不可搶主畫面。
- S11 Requirements — PASS. Requirement Translator 將 User speech bubble 經漏斗轉成 REQ-01/02/03 cards。
- S12 Acceptance Criteria — PASS. Acceptance Owner 拿全空 checklist，另一手阻止 AI 提前蓋 DONE；S22 必須重用同一 checklist 視覺。

## S13–S18 — BUILD
- S13 Context Before Code — PASS. AI Task Director 同時把 PROJECT + SPEC 交給 Agent；左側單一 prompt 漂浮形成錯誤對照。
- S14 Inspect First — ENHANCE. Repository Investigator 的 magnifier 必須對準真實 File Tree/Timestamp/Data Flow clues；所有 files 顯示 locked/unmodified，避免學生誤認 inspect=edit。
- S15 Plan Before Code — PASS. Plan Reviewer 手拿 AI Plan，另一手把 CODE gate 鎖住，Human magnifier 停在 PLAN。
- S16 Human Plan Gate — PASS. Gatekeeper 實際操作 APPROVE/REVISE/REJECT；AI Plan 在左、Code 在右，只有 approve path 可通過。
- S17 Minimal Change — PASS. Implementation Controller 引導 AI 沿窄路抵達 Last Updated，巨大 Refactor cloud 被擋在 scope 外。
- S18 AI Claim ≠ Evidence — ENHANCE. 煥哥像考卷監考者：左側 AI 自己舉 `100 / DONE`，煥哥把它放旁邊，轉身檢查 Changed Files/Diff/Test/AC 四個空 Evidence boxes，強化「AI 不能自己寫答案又自己批改」。

## S19–S23 — VERIFY
- S19 Changed Files — PASS. Change Surface Reviewer 用已核准 Plan checklist 一張張對 Actual file cards；停在 `requirements.txt ?`，Unexpected 是 review signal 而非直接紅叉。
- S20 Diff — PASS. Diff Reviewer magnifier 實際跨過 `- / +`，一手圈合理 Last Updated change，一手標記 dependency version `?`。
- S21 Run/Test — ENHANCE. Tester 必須真的按 RUN，畫面從 Code 切到 Running App，再逐項檢查 Weather loads / Last Updated / existing behavior；呈現 Static→Runtime。
- S22 Return to AC — PASS/CRITICAL. 使用 S12 完全相同 checklist；煥哥拿筆依 Evidence 勾四項，停在 AC-05 FAIL。這是全課最重要 visual callback 之一。
- S23 Human Decision — PASS. Engineering Approver 桌面上同時放 Spec/Diff/Test/AC，根據 evidence 再按 ACCEPT/REVISE/REJECT；視覺鏡像 S16 before-code gate。

## S24–S30 — REMEMBER / LAB / HANDOFF
- S24 Software Needs Memory — PASS. Future Maintainer 面對 final/final2/final_really_final 混亂，手持今天的 Verified Change 卻找不到 Why/Test/Approval；時間軸造成資訊褪色。
- S25 Commit — PASS. Version Historian 親手把 Verified Change 釘成 timeline checkpoint flag；commit message 附著於 checkpoint。
- S26 Git ≠ GitHub — ENHANCE. 煥哥左手操作 Laptop local timeline，右手把 verified checkpoint 推向 GitHub remote repo；用動作呈現 Local History ↔ Shared History，而非單純左右指。
- S27 Engineering Memory — PASS. Project Memory Keeper 將 SPEC/CODE/EVIDENCE/HISTORY 四張卡放入 GitHub vault，旁邊 semester timeline 延伸至 L4/L13/Final。
- S28 Student Mission — PASS. Engineering Coach 站在四 Station 旁，手只指路、不替學生操作；學生 avatar 自己取得四個 Evidence tokens。
- S29 Evidence Package — ENHANCE. Reviewer 不只拿 folder；應逐張掃描 REQUEST/SPEC/AI PLAN/HUMAN REVIEW/DIFF/TEST/AC/GIT HISTORY，缺一張就留下空槽，視覺化 evidence completeness。
- S30 Closing / Handoff — ENHANCE. 煥哥站在完成的 `DEFINE→BUILD→VERIFY→REMEMBER` loop 旁，把同一個 Weather Security Center 交向下一課 UNDERSTAND / later SCAN-FIX-VERIFY road；避免只做 generic victory pose。

## L2 Audit Result
30/30 slides have a valid content-driven visual direction.
Enhancement-required: S01, S03, S06, S09, S14, S18, S21, S26, S29, S30.
These enhancements are canonical requirements for future PPT generation.

## L2 Character Arc
Project Lead → Change Observer → Engineering Lead → Spec Thinker → Change Owner → Engineering Lead → Product Owner → Change Manager → Requirement Investigator → Scope Gatekeeper → Requirement Translator → Acceptance Owner → AI Task Director → Repository Investigator → Plan Reviewer → Human Gatekeeper → Implementation Controller → Engineering Reviewer → Change Surface Reviewer → Diff Reviewer → Tester → Acceptance Verifier → Engineering Approver → Future Maintainer → Version Historian → Engineering Guide → Project Memory Keeper → Engineering Coach → Evidence Reviewer → Course Handoff Guide.

## Mandatory continuity callbacks
- S12 empty AC checklist → S22 same checklist with evidence/results.
- S16 Human Plan Gate → S23 Human Evidence Gate.
- S06 four-layer map → S28 four-station Lab.
- S01 `WORKING ≠ MANAGED` → S30 completed managed-change loop.

Rule: if a PPT generator replaces these callbacks with unrelated generic illustrations, the visual design fails even if the text remains correct.