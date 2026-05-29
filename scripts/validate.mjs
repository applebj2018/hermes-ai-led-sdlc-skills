#!/usr/bin/env node
/**
 * 校验 Skill 包格式
 * 检查项：
 * 1. 每个 skills/ 子目录必须有 SKILL.md
 * 2. SKILL.md 必须有 YAML frontmatter（name, description, version）
 * 3. catalog.json 与 .well-known/skills/index.json 中的技能列表一致
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const skillsDir = path.join(__dirname, '..', 'skills');
const catalogPath = path.join(__dirname, '..', 'catalog.json');
const indexPath = path.join(__dirname, '..', '.well-known', 'skills', 'index.json');

let exitCode = 0;
const errors = [];

function logError(msg) {
  errors.push(msg);
  console.error('\u274C ' + msg);
  exitCode = 1;
}

function logOK(msg) {
  console.log('\u2705 ' + msg);
}

// 1. 读取目录
const skillDirs = fs.readdirSync(skillsDir).filter(d => {
  const stat = fs.statSync(path.join(skillsDir, d));
  return stat.isDirectory() && !d.startsWith('.');
});

console.log('\ud83d\udd0d 发现 ' + skillDirs.length + ' 个技能目录\n');

// 2. 检查每个技能
for (const dir of skillDirs) {
  const skillPath = path.join(skillsDir, dir);
  const skillMdPath = path.join(skillPath, 'SKILL.md');

  if (!fs.existsSync(skillMdPath)) {
    logError(dir + ': 缺少 SKILL.md');
    continue;
  }

  const content = fs.readFileSync(skillMdPath, 'utf8');

  // 检查 frontmatter
  if (!content.startsWith('---')) {
    logError(dir + '/SKILL.md: 缺少 YAML frontmatter');
    continue;
  }

  const fmMatch = content.match(/^---\s*\n([\s\S]*?)\n---/);
  if (!fmMatch) {
    logError(dir + '/SKILL.md: frontmatter 格式错误');
    continue;
  }

  const fm = fmMatch[1];
  const requiredFields = ['name', 'description', 'version'];
  for (const field of requiredFields) {
    if (!fm.includes(field + ':')) {
      logError(dir + '/SKILL.md: frontmatter 缺少 ' + field);
    }
  }

  logOK(dir + ': SKILL.md 格式正确');
}

// 3. 检查 catalog.json
const catalog = JSON.parse(fs.readFileSync(catalogPath, 'utf8'));
const catalogNames = catalog.skills.map(s => s.name).sort();
const dirNames = skillDirs.sort();

if (JSON.stringify(catalogNames) !== JSON.stringify(dirNames)) {
  logError('catalog.json 中的技能列表与 skills/ 目录不一致');
  console.error('  catalog: ' + JSON.stringify(catalogNames));
  console.error('  dirs:    ' + JSON.stringify(dirNames));
} else {
  logOK('catalog.json 与目录结构一致');
}

// 4. 检查 index.json
const index = JSON.parse(fs.readFileSync(indexPath, 'utf8'));
const indexNames = index.skills.map(s => s.name).sort();

if (JSON.stringify(indexNames) !== JSON.stringify(dirNames)) {
  logError('.well-known/skills/index.json 中的技能列表与 skills/ 目录不一致');
} else {
  logOK('.well-known/skills/index.json 与目录结构一致');
}

console.log('\n' + (errors.length === 0 ? '\u2705 全部通过' : '\u274C 发现 ' + errors.length + ' 个问题'));
process.exit(exitCode);
