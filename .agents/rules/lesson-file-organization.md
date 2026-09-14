# Rule: Lecture Chapter File Organization

## 📌 Core Rule
All files relating to a specific lecture chapter/lesson (e.g. `Lesson0`, `Lesson1`, ... `Lesson16`) **MUST be located inside or organized directly under that lesson's dedicated directory** (`Lesson0/`, `Lesson1/`, ... `Lesson16/`).

## 📂 Required Directory Layout for Each Lesson
For any lesson `Lesson{N}`:

```text
Lesson{N}/
├── README.md                              # Main lecture outline & canonical script
├── AIIS_L{N}_Orientation_Presentation.pptx # Generated presentation slide deck
├── AIIS_L{N}_FIGURE_GENERATOR.yaml        # Visual & diagram specification
├── AIIS_L{N}.png                          # Infographic roadmap / hero image (if applicable)
├── assets/                                # Specific visual assets, avatars, screenshots
├── scripts/                               # Presentation generators or lesson demo code
└── planning/                              # Detailed teaching scripts, visual audits, and complete markers
```

## 🚫 Prohibitions
1. **No Stray Chapter Files in Root**: Do not leave `AIIS_L0.png`, `AIIS_L1_demo.py`, or similar lesson-specific artifacts in the workspace root or repository root.
2. **Canonical Consolidation**: Whenever a new lesson is planned or implemented, all its slides, scripts, YAML specs, images, and presentation decks must be moved to/placed in `Lesson{N}/`.
3. **Traceability**: If cross-lesson planning files exist in `_myplan_`, the lesson-specific implementation and teaching deliverables must be mirrored/moved to the corresponding `Lesson{N}/`.
