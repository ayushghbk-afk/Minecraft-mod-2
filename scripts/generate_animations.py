#!/usr/bin/env python3
"""Write Bedrock animation overrides that give vanilla mobs more weight.

The files keep vanilla animation identifiers so they replace the stock poses
without copying client-entity files (those break on engine updates). Extra
motion is driven by the same Molang variables vanilla already sets, so idle
poses stay still and attacks only wind up while attack_time is non-zero.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANIM = ROOT / "packs" / "realistic_sticks_rp" / "animations"

# Shared attack curves. Vanilla attack_time runs 0 -> 1 during a swing.
# STRIKE peaks near the hit; TWIST is the torso yaw that sells follow-through.
STRIKE = (
    "(math.sin((1.0 - math.pow(1.0 - variable.attack_time, 3.0)) * 180.0) * 1.25 "
    "+ math.sin(variable.attack_time * 180.0) * 0.35)"
)
TWIST = "math.sin(math.sqrt(variable.attack_time) * 360.0)"
LUNGE = "math.sin(variable.attack_time * 180.0)"
# Zombie / vindicator vanilla-style punch (sin attack + recovery sin).
Z_PUNCH = (
    "(math.sin(variable.attack_time * 180.0) * 1.45 "
    "- math.sin((1.0 - (1.0 - variable.attack_time) * (1.0 - variable.attack_time)) * 180.0) * 0.5)"
)


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def humanoid() -> dict:
    return {
        "format_version": "1.8.0",
        "animations": {
            "animation.humanoid.attack.rotations": {
                "loop": True,
                "bones": {
                    "body": {
                        "rotation": [
                            f"{LUNGE} * 8.0",
                            f"{TWIST} * 22.0 - this",
                            f"{TWIST} * -4.0",
                        ],
                        "position": [0.0, f"{LUNGE} * -0.7", f"{LUNGE} * 1.6"],
                    },
                    "head": {
                        "rotation": [f"{LUNGE} * 10.0", f"{TWIST} * 6.0", 0.0],
                    },
                    "leftarm": {
                        "rotation": [
                            f"{STRIKE} * 18.0",
                            f"{TWIST} * -8.0",
                            f"{LUNGE} * 12.0",
                        ],
                    },
                    "rightarm": {
                        "rotation": [
                            f"{STRIKE} * (variable.is_brandishing_spear || variable.is_holding_spyglass ? -70.0 : 78.0)",
                            f"variable.is_brandishing_spear || variable.is_holding_spyglass ? 0.0 : ({TWIST} * 28.0)",
                            f"{LUNGE} * -16.0",
                        ],
                    },
                    "leftleg": {
                        "rotation": [f"{LUNGE} * -10.0", 0.0, 0.0],
                    },
                    "rightleg": {
                        "rotation": [f"{LUNGE} * 8.0", 0.0, 0.0],
                    },
                },
            },
            "animation.humanoid.move": {
                "loop": True,
                "bones": {
                    "body": {
                        "rotation": [
                            "math.abs(variable.tcos0) * 0.04",
                            "variable.tcos0 * 0.12",
                            "variable.tcos0 * 0.05",
                        ],
                        "position": [0.0, "math.abs(variable.tcos0) * 0.018", 0.0],
                    },
                    "head": {
                        "rotation": ["math.abs(variable.tcos0) * 0.03", 0.0, "variable.tcos0 * -0.04"],
                    },
                    "leftarm": {"rotation": ["variable.tcos0 * 1.35", 0.0, "variable.tcos0 * 0.08"]},
                    "rightarm": {"rotation": ["-variable.tcos0 * 1.35", 0.0, "variable.tcos0 * 0.08"]},
                    "leftleg": {"rotation": ["variable.tcos0 * -1.65", -0.1, -0.1]},
                    "rightleg": {"rotation": ["variable.tcos0 * 1.65", 0.1, 0.1]},
                },
            },
            "animation.humanoid.bob": {
                "loop": True,
                "bones": {
                    "body": {
                        "position": [0.0, "math.sin(query.life_time * 90.0) * 0.28", 0.0],
                    },
                    "leftarm": {
                        "rotation": [0.0, 0.0, "((math.cos(query.life_time * 103.2) * 3.6) + 3.6) * -1.0"],
                    },
                    "rightarm": {
                        "rotation": [0.0, 0.0, "(math.cos(query.life_time * 103.2) * 3.6) + 3.6"],
                    },
                },
            },
        },
    }


def player() -> dict:
    return {
        "format_version": "1.8.0",
        "animations": {
            "animation.player.attack.positions": {
                "loop": True,
                "bones": {
                    "head": {"rotation": [f"{LUNGE} * 8.0", 0.0, 0.0]},
                    "body": {
                        "position": [0.0, f"{LUNGE} * -0.85", f"{LUNGE} * 2.2"],
                    },
                    "waist": {
                        "position": [0.0, 0.0, f"{LUNGE} * 1.1"],
                    },
                },
            },
            "animation.player.attack.rotations": {
                "loop": True,
                "bones": {
                    "body": {
                        "rotation": [
                            f"{LUNGE} * 10.0",
                            "variable.attack_body_rot_y * 1.35",
                            f"{TWIST} * -6.0",
                        ],
                    },
                    "head": {
                        "rotation": [f"{LUNGE} * 6.0", f"{TWIST} * 4.0", 0.0],
                    },
                    "leftarm": {
                        "rotation": [
                            f"-({STRIKE}) * 16.0",
                            f"{TWIST} * -10.0",
                            f"{LUNGE} * 14.0",
                        ],
                    },
                    "rightarm": {
                        "rotation": [
                            f"-({STRIKE}) * 52.0",
                            (
                                "-(math.sin((1.0 - math.pow((1.0 - variable.attack_time), 4.0)) * 180.0) "
                                "? (-105.0 * math.sin((1.0 - math.pow((1.0 - variable.attack_time), 4.0)) * 180.0)) + 36.0 "
                                ": 0.0)"
                            ),
                            f"{LUNGE} * -22.0",
                        ],
                    },
                    "leftleg": {"rotation": [f"{LUNGE} * -8.0", -0.1, -0.1]},
                    "rightleg": {"rotation": [f"{LUNGE} * 10.0", 0.1, 0.1]},
                },
            },
            "animation.player.bob": {
                "loop": True,
                "bones": {
                    "body": {
                        "position": [0.0, "math.sin(query.life_time * 90.0) * 0.32", 0.0],
                    },
                    "leftarm": {
                        "rotation": [0.0, 0.0, "-((math.cos(query.life_time * 103.2) * 3.6) + 3.6)"],
                    },
                    "rightarm": {
                        "rotation": [0.0, 0.0, "(math.cos(query.life_time * 103.2) * 3.6) + 3.6"],
                    },
                },
            },
            "animation.player.move.arms": {
                "loop": True,
                "bones": {
                    "leftarm": {"rotation": ["variable.tcos0 * 1.4", 0.0, "variable.tcos0 * 0.1"]},
                    "rightarm": {"rotation": ["-variable.tcos0 * 1.4", 0.0, "variable.tcos0 * 0.1"]},
                    "body": {
                        "rotation": [
                            "math.abs(variable.tcos0) * 0.045",
                            "variable.tcos0 * 0.14",
                            "variable.tcos0 * 0.06",
                        ],
                        "position": [0.0, "math.abs(variable.tcos0) * 0.02", 0.0],
                    },
                },
            },
            "animation.player.move.legs": {
                "loop": True,
                "bones": {
                    "leftleg": {"rotation": ["variable.tcos0 * -1.7", -0.1, -0.1]},
                    "rightleg": {"rotation": ["variable.tcos0 * 1.7", 0.1, 0.1]},
                },
            },
        },
    }


def player_firstperson() -> dict:
    factor = "variable.first_person_item_rotation_factor"
    return {
        "format_version": "1.8.0",
        "animations": {
            "animation.player.first_person.attack_rotation": {
                "loop": True,
                "bones": {
                    "rightarm": {
                        "position": [
                            f"math.clamp(-20.0 * math.sin({factor} * variable.attack_time * 112.0), -9.0, 999.0) * math.sin({factor} * variable.attack_time * 112.0)",
                            f"math.sin({factor} * (1.0 - variable.attack_time) * (1.0 - variable.attack_time) * 200.0) * 10.5 - {factor} * variable.attack_time * 18.0 + variable.short_arm_offset_right",
                            f"math.sin({factor} * variable.attack_time * 120.0) * 3.2",
                        ],
                        "rotation": [
                            f"math.sin({factor} * (1.0 - variable.attack_time) * (1.0 - variable.attack_time) * 280.0) * -92.0",
                            f"math.sin({factor} * (1.0 - variable.attack_time) * (1.0 - variable.attack_time) * 280.0) * 58.0",
                            f"math.sin({factor} * (1.0 - variable.attack_time) * (1.0 - variable.attack_time) * 280.0) * 34.0",
                        ],
                    },
                },
            },
            "animation.player.first_person.attack_rotation_item": {
                "loop": True,
                "override_previous_animation": True,
                "bones": {
                    "rightitem": {
                        "position": [
                            "-math.sin(math.sqrt(variable.attack_time) * math.pi * 100.0) * 14.0",
                            "math.sin(math.sqrt(variable.attack_time) * math.pi * 2.0 * 60.0) * 14.0",
                            "-math.sin(variable.attack_time * math.pi * 65.0) * 3.5",
                        ],
                        "rotation": [
                            "-math.sin(math.sqrt(variable.attack_time) * math.pi * 20.0) * 38.0",
                            "-math.sin(math.sqrt(variable.attack_time) * 75.0) * 24.0",
                            "-math.sin(math.sqrt(variable.attack_time) * 25.0) * 22.0",
                        ],
                    },
                },
            },
        },
    }


def zombie() -> dict:
    life_x = "math.sin(query.life_time * 76.776372) * 2.865"
    life_z = "math.cos(query.life_time * 103.13244) * 2.865"
    return {
        "format_version": "1.8.0",
        "animations": {
            "animation.zombie.attack_bare_hand": {
                "loop": True,
                "bones": {
                    "body": {
                        "rotation": [f"{LUNGE} * 16.0", f"{LUNGE} * 7.0", 0.0],
                        "position": [0.0, f"{LUNGE} * -1.1", f"{LUNGE} * 2.8"],
                    },
                    "head": {
                        "rotation": [f"{LUNGE} * 14.0", 0.0, 0.0],
                    },
                    "leftarm": {
                        "rotation": [
                            f"-90.0 - ((math.sin(variable.attack_time * 180.0) * 57.3) * 1.55 - (math.sin((1.0 - (1.0 - variable.attack_time) * (1.0 - variable.attack_time)) * 180.0) * 57.3) * 0.5) - ({life_x}) - this",
                            f"8.6 - ((math.sin(variable.attack_time * 180.0) * 57.3) * 0.85) - this",
                            f"{life_z} * -1.0 - 2.865 - this",
                        ],
                    },
                    "rightarm": {
                        "rotation": [
                            f"90.0 * (variable.is_brandishing_spear - 1.0) - ((math.sin(variable.attack_time * 180.0) * 57.3) * 1.55 - (math.sin((1.0 - (1.0 - variable.attack_time) * (1.0 - variable.attack_time)) * 180.0) * 57.3) * 0.5) + ({life_x}) - this",
                            f"(math.sin(variable.attack_time * 180.0) * 57.3) * 0.85 - 8.6 - this",
                            f"{life_z} + 2.865 - this",
                        ],
                    },
                },
            },
            "animation.zombie.baby_attack_bare_hand": {
                "loop": True,
                "bones": {
                    "body": {
                        "rotation": [f"{LUNGE} * 12.0", 0.0, 0.0],
                        "position": [0.0, 0.0, f"{LUNGE} * 1.8"],
                    },
                    "leftarm": {
                        "rotation": [
                            f"-((math.sin(variable.attack_time * 180.0) * 57.3) * 1.45 - (math.sin((1.0 - (1.0 - variable.attack_time) * (1.0 - variable.attack_time)) * 180.0) * 57.3) * 0.5) - ({life_x}) - this",
                            f"8.6 - ((math.sin(variable.attack_time * 180.0) * 57.3) * 0.8) - this",
                            f"{life_z} * -1.0 - 2.865 - this",
                        ],
                    },
                    "rightarm": {
                        "rotation": [
                            f"-((math.sin(variable.attack_time * 180.0) * 57.3) * 1.45 - (math.sin((1.0 - (1.0 - variable.attack_time) * (1.0 - variable.attack_time)) * 180.0) * 57.3) * 0.5) + ({life_x}) - this",
                            f"(math.sin(variable.attack_time * 180.0) * 57.3) * 0.8 - 8.6 - this",
                            f"{life_z} + 2.865 - this",
                        ],
                    },
                },
            },
        },
    }


def quadruped() -> dict:
    # Diagonal gait already matches real quadrupeds (leg0+leg3, leg1+leg2).
    # Extra body bounce and head nod make cows, pigs, and sheep look alive.
    return {
        "format_version": "1.8.0",
        "animations": {
            "animation.quadruped.walk": {
                "anim_time_update": "query.modified_distance_moved",
                "loop": True,
                "bones": {
                    "body": {
                        "rotation": [
                            "math.sin(query.anim_time * 76.34) * 5.5",
                            0.0,
                            "math.cos(query.anim_time * 38.17) * 4.0",
                        ],
                        "position": [0.0, "math.abs(math.sin(query.anim_time * 38.17)) * 1.35", 0.0],
                    },
                    "head": {
                        "rotation": ["math.sin(query.anim_time * 38.17) * 10.0", 0.0, "math.cos(query.anim_time * 38.17) * 3.0"],
                    },
                    "leg0": {"rotation": ["math.cos(query.anim_time * 38.17) * 88.0", 0.0, "math.sin(query.anim_time * 38.17) * 5.0"]},
                    "leg1": {"rotation": ["math.cos(query.anim_time * 38.17) * -88.0", 0.0, "math.sin(query.anim_time * 38.17) * -5.0"]},
                    "leg2": {"rotation": ["math.cos(query.anim_time * 38.17) * -88.0", 0.0, "math.sin(query.anim_time * 38.17) * 5.0"]},
                    "leg3": {"rotation": ["math.cos(query.anim_time * 38.17) * 88.0", 0.0, "math.sin(query.anim_time * 38.17) * -5.0"]},
                },
            },
        },
    }


def creeper() -> dict:
    return {
        "format_version": "1.8.0",
        "animations": {
            "animation.creeper.legs": {
                "loop": True,
                "bones": {
                    "body": {
                        "rotation": [0.0, "variable.leg_rot * 0.12", "variable.leg_rot * 0.18"],
                        "position": [0.0, "math.abs(variable.leg_rot) * 0.012", 0.0],
                    },
                    "head": {
                        "rotation": ["math.abs(variable.leg_rot) * 0.08", 0.0, "variable.leg_rot * -0.1"],
                    },
                    "leg0": {"rotation": ["variable.leg_rot * 1.15 - this", 0.0, 0.0]},
                    "leg1": {"rotation": ["-variable.leg_rot * 1.15 - this", 0.0, 0.0]},
                    "leg2": {"rotation": ["-variable.leg_rot * 1.15 - this", 0.0, 0.0]},
                    "leg3": {"rotation": ["variable.leg_rot * 1.15 - this", 0.0, 0.0]},
                },
            },
        },
    }


def spider() -> dict:
    # Alternating tetrapod waves, larger lift, plus a crawling body bob.
    def leg(index: int, sign_y: str, sign_z: str) -> dict:
        phase = index // 2
        return {
            "rotation": [
                0.0,
                f"{sign_y}math.abs(math.cos(query.anim_time * 76.34 + 90.0 * {phase}) * 32.0)",
                f"{sign_z}math.abs(math.sin(query.anim_time * 38.17 + 90.0 * {phase}) * 32.0)",
            ],
        }

    return {
        "format_version": "1.8.0",
        "animations": {
            "animation.spider.walk": {
                "anim_time_update": "query.modified_distance_moved",
                "loop": True,
                "bones": {
                    "body": {
                        "position": [0.0, "math.abs(math.sin(query.anim_time * 76.34)) * 0.9", 0.0],
                        "rotation": [0.0, 0.0, "math.sin(query.anim_time * 38.17) * 4.0"],
                    },
                    "head": {
                        "rotation": ["math.sin(query.anim_time * 38.17) * 6.0", 0.0, 0.0],
                    },
                    "leg0": leg(0, "-", ""),
                    "leg1": leg(1, "", "-"),
                    "leg2": leg(2, "-", ""),
                    "leg3": leg(3, "", "-"),
                    "leg4": leg(4, "-", ""),
                    "leg5": leg(5, "", "-"),
                    "leg6": leg(6, "-", ""),
                    "leg7": leg(7, "", "-"),
                },
            },
        },
    }


def iron_golem() -> dict:
    smash = "((1.5 * math.abs(math.mod(variable.attack_animation_tick - query.frame_alpha, 10.0) - 5.0) - 2.5) / 5.0)"
    return {
        "format_version": "1.8.0",
        "animations": {
            "animation.iron_golem.attack": {
                "loop": True,
                "bones": {
                    "body": {
                        "rotation": [f"{smash} * 28.0", 0.0, 0.0],
                        "position": [0.0, f"{smash} * -2.5", f"{smash} * 3.0"],
                    },
                    "head": {
                        "rotation": [f"{smash} * 12.0", 0.0, 0.0],
                    },
                    "arm0": {
                        "rotation": [f"-125.0 + {smash} * 70.0", 0.0, f"{smash} * -8.0"],
                    },
                    "arm1": {
                        "rotation": [f"-125.0 + {smash} * 70.0", 0.0, f"{smash} * 8.0"],
                    },
                    "leg0": {"rotation": [f"{smash} * -6.0", 0.0, 0.0]},
                    "leg1": {"rotation": [f"{smash} * 6.0", 0.0, 0.0]},
                },
            },
            "animation.iron_golem.walk": {
                "loop": True,
                "bones": {
                    "body": {
                        "rotation": [0.0, 0.0, "variable.modified_tcos0 / 1.15"],
                        "position": [0.0, "math.abs(variable.modified_tcos0) * 0.08", 0.0],
                    },
                    "head": {"rotation": [0.0, 0.0, "variable.modified_tcos0 / 1.35"]},
                    "leg0": {"rotation": ["variable.modified_tcos0 * 7.2", 0.0, 0.0]},
                    "leg1": {"rotation": ["-variable.modified_tcos0 * 7.2", 0.0, 0.0]},
                },
            },
            "animation.iron_golem.move": {
                "loop": True,
                "bones": {
                    "arm0": {"rotation": ["-variable.modified_tcos0 * 2.6", 0.0, 0.0]},
                    "arm1": {"rotation": ["variable.modified_tcos0 * 2.6", 0.0, 0.0]},
                },
            },
        },
    }


def vindicator() -> dict:
    return {
        "format_version": "1.8.0",
        "animations": {
            "animation.vindicator.attack": {
                "loop": True,
                "bones": {
                    "body": {
                        "rotation": [f"{LUNGE} * 12.0", f"{TWIST} * 16.0", 0.0],
                        "position": [0.0, f"{LUNGE} * -0.8", f"{LUNGE} * 1.8"],
                    },
                    "head": {"rotation": [f"{LUNGE} * 8.0", 0.0, 0.0]},
                    "leftarm": {
                        "rotation": [
                            f"query.is_riding ? 0.0 : ((math.cos(query.life_time * 20.0 * 10.89) * 28.65) + ({Z_PUNCH} * 57.3))",
                            f"{TWIST} * -6.0",
                            0.0,
                        ],
                    },
                    "rightarm": {
                        "rotation": [
                            f"(-118.0 + math.cos(query.life_time * 20.0 * 3.84) * 2.87) + ({Z_PUNCH} * 90.0)",
                            f"{TWIST} * 10.0",
                            f"{LUNGE} * -18.0",
                        ],
                    },
                },
            },
            "animation.vindicator.hand_attack": {
                "loop": True,
                "bones": {
                    "body": {
                        "rotation": [f"{LUNGE} * 14.0", 0.0, 0.0],
                        "position": [0.0, 0.0, f"{LUNGE} * 2.0"],
                    },
                    "leftarm": {
                        "rotation": [
                            f"(-118.0 + math.cos(query.life_time * 20.0 * 3.84) * 2.87) + ({Z_PUNCH} * 90.0)",
                            0.0,
                            f"{LUNGE} * 16.0",
                        ],
                    },
                    "rightarm": {
                        "rotation": [
                            f"(-118.0 + math.cos(query.life_time * 20.0 * 3.84) * 2.87) + ({Z_PUNCH} * 90.0)",
                            0.0,
                            f"{LUNGE} * -16.0",
                        ],
                    },
                },
            },
            "animation.vindicator.walk": {
                "loop": True,
                "bones": {
                    "body": {
                        "rotation": [0.0, 0.0, "math.cos(query.modified_distance_moved * 38.17) * 3.5 * query.modified_move_speed"],
                        "position": [0.0, "math.abs(math.cos(query.modified_distance_moved * 38.17)) * 0.7 * query.modified_move_speed", 0.0],
                    },
                    "leg0": {
                        "rotation": [
                            "(math.cos(query.modified_distance_moved * 38.17) * 92.0) * query.modified_move_speed * 0.5",
                            0.0,
                            0.0,
                        ],
                    },
                    "leg1": {
                        "rotation": [
                            "(math.cos(query.modified_distance_moved * 38.17 + 180.0) * 92.0) * query.modified_move_speed * 0.5",
                            0.0,
                            0.0,
                        ],
                    },
                },
            },
        },
    }


def chicken() -> dict:
    return {
        "format_version": "1.8.0",
        "animations": {
            "animation.chicken.move": {
                "anim_time_update": "query.modified_distance_moved",
                "loop": True,
                "bones": {
                    "body": {
                        "rotation": ["math.sin(query.anim_time * 76.34) * 6.0", 0.0, "math.cos(query.anim_time * 38.17) * 4.0"],
                        "position": [0.0, "math.abs(math.sin(query.anim_time * 38.17)) * 1.1", 0.0],
                    },
                    "head": {
                        "rotation": ["math.sin(query.anim_time * 38.17) * 16.0", 0.0, 0.0],
                    },
                    "leg0": {"rotation": ["math.cos(query.anim_time * 38.17) * 92.0", 0.0, 0.0]},
                    "leg1": {"rotation": ["math.cos(query.anim_time * 38.17) * -92.0", 0.0, 0.0]},
                },
            },
        },
    }


FILES = {
    "humanoid.animation.json": humanoid,
    "player.animation.json": player,
    "player_firstperson.animation.json": player_firstperson,
    "zombie.animation.json": zombie,
    "quadruped.animation.json": quadruped,
    "creeper.animation.json": creeper,
    "spider.animation.json": spider,
    "iron_golem.animation.json": iron_golem,
    "vindicator.animation.json": vindicator,
    "chicken.animation.json": chicken,
}


def main() -> None:
    ANIM.mkdir(parents=True, exist_ok=True)
    total = 0
    for name, builder in FILES.items():
        data = builder()
        dump(ANIM / name, data)
        total += len(data["animations"])
    print(f"Generated {len(FILES)} animation files with {total} animation overrides.")


if __name__ == "__main__":
    main()
